from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppRegistration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appIdentifier: SerializeAsAny[Optional[MobileAppIdentifier]] = Field(default=None,alias="appIdentifier",)
	applicationVersion: Optional[str] = Field(default=None,alias="applicationVersion",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	deviceTag: Optional[str] = Field(default=None,alias="deviceTag",)
	deviceType: Optional[str] = Field(default=None,alias="deviceType",)
	flaggedReasons: Optional[list[ManagedAppFlaggedReason]] = Field(default=None,alias="flaggedReasons",)
	lastSyncDateTime: Optional[datetime] = Field(default=None,alias="lastSyncDateTime",)
	managementSdkVersion: Optional[str] = Field(default=None,alias="managementSdkVersion",)
	platformVersion: Optional[str] = Field(default=None,alias="platformVersion",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	version: Optional[str] = Field(default=None,alias="version",)
	appliedPolicies: Optional[list[ManagedAppPolicy]] = Field(default=None,alias="appliedPolicies",)
	intendedPolicies: Optional[list[ManagedAppPolicy]] = Field(default=None,alias="intendedPolicies",)
	operations: Optional[list[ManagedAppOperation]] = Field(default=None,alias="operations",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.androidManagedAppRegistration":
				from .android_managed_app_registration import AndroidManagedAppRegistration
				return AndroidManagedAppRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosManagedAppRegistration":
				from .ios_managed_app_registration import IosManagedAppRegistration
				return IosManagedAppRegistration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mobile_app_identifier import MobileAppIdentifier
from .managed_app_flagged_reason import ManagedAppFlaggedReason
from .managed_app_policy import ManagedAppPolicy
from .managed_app_policy import ManagedAppPolicy
from .managed_app_operation import ManagedAppOperation

