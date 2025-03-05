from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[str] = Field(default=None,alias="version",)

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
			if mapping_key == "#microsoft.graph.managedAppConfiguration":
				from .managed_app_configuration import ManagedAppConfiguration
				return ManagedAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppConfiguration":
				from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
				return TargetedManagedAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppProtection":
				from .managed_app_protection import ManagedAppProtection
				return ManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.defaultManagedAppProtection":
				from .default_managed_app_protection import DefaultManagedAppProtection
				return DefaultManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppProtection":
				from .targeted_managed_app_protection import TargetedManagedAppProtection
				return TargetedManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedAppProtection":
				from .android_managed_app_protection import AndroidManagedAppProtection
				return AndroidManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.iosManagedAppProtection":
				from .ios_managed_app_protection import IosManagedAppProtection
				return IosManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtection":
				from .windows_information_protection import WindowsInformationProtection
				return WindowsInformationProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.mdmWindowsInformationProtectionPolicy":
				from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
				return MdmWindowsInformationProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionPolicy":
				from .windows_information_protection_policy import WindowsInformationProtectionPolicy
				return WindowsInformationProtectionPolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


