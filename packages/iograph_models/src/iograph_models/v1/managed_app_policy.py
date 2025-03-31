from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ManagedAppPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

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
			if mapping_key == "#microsoft.graph.targetedManagedAppConfiguration":
				from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
				return TargetedManagedAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.defaultManagedAppProtection":
				from .default_managed_app_protection import DefaultManagedAppProtection
				return DefaultManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedAppProtection":
				from .android_managed_app_protection import AndroidManagedAppProtection
				return AndroidManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.iosManagedAppProtection":
				from .ios_managed_app_protection import IosManagedAppProtection
				return IosManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.mdmWindowsInformationProtectionPolicy":
				from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
				return MdmWindowsInformationProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionPolicy":
				from .windows_information_protection_policy import WindowsInformationProtectionPolicy
				return WindowsInformationProtectionPolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

