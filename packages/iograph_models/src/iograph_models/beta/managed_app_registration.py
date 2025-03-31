from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ManagedAppRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appIdentifier: Optional[Union[AndroidMobileAppIdentifier, IosMobileAppIdentifier, MacAppIdentifier, WindowsAppIdentifier]] = Field(alias="appIdentifier", default=None,discriminator="odata_type", )
	applicationVersion: Optional[str] = Field(alias="applicationVersion", default=None,)
	azureADDeviceId: Optional[str] = Field(alias="azureADDeviceId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deviceManufacturer: Optional[str] = Field(alias="deviceManufacturer", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceTag: Optional[str] = Field(alias="deviceTag", default=None,)
	deviceType: Optional[str] = Field(alias="deviceType", default=None,)
	flaggedReasons: Optional[list[ManagedAppFlaggedReason | str]] = Field(alias="flaggedReasons", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managementSdkVersion: Optional[str] = Field(alias="managementSdkVersion", default=None,)
	platformVersion: Optional[str] = Field(alias="platformVersion", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	appliedPolicies: Optional[list[Annotated[Union[TargetedManagedAppConfiguration, DefaultManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy, WindowsManagedAppProtection],Field(discriminator="odata_type")]]] = Field(alias="appliedPolicies", default=None,)
	intendedPolicies: Optional[list[Annotated[Union[TargetedManagedAppConfiguration, DefaultManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy, WindowsManagedAppProtection],Field(discriminator="odata_type")]]] = Field(alias="intendedPolicies", default=None,)
	managedAppLogCollectionRequests: Optional[list[ManagedAppLogCollectionRequest]] = Field(alias="managedAppLogCollectionRequests", default=None,)
	operations: Optional[list[ManagedAppOperation]] = Field(alias="operations", default=None,)

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
			if mapping_key == "#microsoft.graph.windowsManagedAppRegistration":
				from .windows_managed_app_registration import WindowsManagedAppRegistration
				return WindowsManagedAppRegistration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .android_mobile_app_identifier import AndroidMobileAppIdentifier
from .ios_mobile_app_identifier import IosMobileAppIdentifier
from .mac_app_identifier import MacAppIdentifier
from .windows_app_identifier import WindowsAppIdentifier
from .managed_app_flagged_reason import ManagedAppFlaggedReason
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .default_managed_app_protection import DefaultManagedAppProtection
from .android_managed_app_protection import AndroidManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .windows_managed_app_protection import WindowsManagedAppProtection
from .managed_app_log_collection_request import ManagedAppLogCollectionRequest
from .managed_app_operation import ManagedAppOperation
