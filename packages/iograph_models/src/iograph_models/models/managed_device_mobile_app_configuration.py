from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDeviceMobileAppConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	targetedMobileApps: Optional[list[str]] = Field(default=None,alias="targetedMobileApps",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[ManagedDeviceMobileAppConfigurationAssignment]] = Field(default=None,alias="assignments",)
	deviceStatuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusSummary: Optional[ManagedDeviceMobileAppConfigurationDeviceSummary] = Field(default=None,alias="deviceStatusSummary",)
	userStatuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusSummary: Optional[ManagedDeviceMobileAppConfigurationUserSummary] = Field(default=None,alias="userStatusSummary",)

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
			if mapping_key == "#microsoft.graph.iosMobileAppConfiguration":
				from .ios_mobile_app_configuration import IosMobileAppConfiguration
				return IosMobileAppConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

