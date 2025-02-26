from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class TargetedManagedAppProtection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[str] = Field(default=None,alias="version",)
	allowedDataStorageLocations: list[ManagedAppDataStorageLocation] = Field(alias="allowedDataStorageLocations",)
	allowedInboundDataTransferSources: Optional[ManagedAppDataTransferLevel] = Field(default=None,alias="allowedInboundDataTransferSources",)
	allowedOutboundClipboardSharingLevel: Optional[ManagedAppClipboardSharingLevel] = Field(default=None,alias="allowedOutboundClipboardSharingLevel",)
	allowedOutboundDataTransferDestinations: Optional[ManagedAppDataTransferLevel] = Field(default=None,alias="allowedOutboundDataTransferDestinations",)
	contactSyncBlocked: Optional[bool] = Field(default=None,alias="contactSyncBlocked",)
	dataBackupBlocked: Optional[bool] = Field(default=None,alias="dataBackupBlocked",)
	deviceComplianceRequired: Optional[bool] = Field(default=None,alias="deviceComplianceRequired",)
	disableAppPinIfDevicePinIsSet: Optional[bool] = Field(default=None,alias="disableAppPinIfDevicePinIsSet",)
	fingerprintBlocked: Optional[bool] = Field(default=None,alias="fingerprintBlocked",)
	managedBrowser: Optional[ManagedBrowserType] = Field(default=None,alias="managedBrowser",)
	managedBrowserToOpenLinksRequired: Optional[bool] = Field(default=None,alias="managedBrowserToOpenLinksRequired",)
	maximumPinRetries: Optional[int] = Field(default=None,alias="maximumPinRetries",)
	minimumPinLength: Optional[int] = Field(default=None,alias="minimumPinLength",)
	minimumRequiredAppVersion: Optional[str] = Field(default=None,alias="minimumRequiredAppVersion",)
	minimumRequiredOsVersion: Optional[str] = Field(default=None,alias="minimumRequiredOsVersion",)
	minimumWarningAppVersion: Optional[str] = Field(default=None,alias="minimumWarningAppVersion",)
	minimumWarningOsVersion: Optional[str] = Field(default=None,alias="minimumWarningOsVersion",)
	organizationalCredentialsRequired: Optional[bool] = Field(default=None,alias="organizationalCredentialsRequired",)
	periodBeforePinReset: Optional[str] = Field(default=None,alias="periodBeforePinReset",)
	periodOfflineBeforeAccessCheck: Optional[str] = Field(default=None,alias="periodOfflineBeforeAccessCheck",)
	periodOfflineBeforeWipeIsEnforced: Optional[str] = Field(default=None,alias="periodOfflineBeforeWipeIsEnforced",)
	periodOnlineBeforeAccessCheck: Optional[str] = Field(default=None,alias="periodOnlineBeforeAccessCheck",)
	pinCharacterSet: Optional[ManagedAppPinCharacterSet] = Field(default=None,alias="pinCharacterSet",)
	pinRequired: Optional[bool] = Field(default=None,alias="pinRequired",)
	printBlocked: Optional[bool] = Field(default=None,alias="printBlocked",)
	saveAsBlocked: Optional[bool] = Field(default=None,alias="saveAsBlocked",)
	simplePinBlocked: Optional[bool] = Field(default=None,alias="simplePinBlocked",)
	isAssigned: Optional[bool] = Field(default=None,alias="isAssigned",)
	assignments: list[TargetedManagedAppPolicyAssignment] = Field(alias="assignments",)

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
			if mapping_key == "#microsoft.graph.androidManagedAppProtection":
				from .android_managed_app_protection import AndroidManagedAppProtection
				return AndroidManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.iosManagedAppProtection":
				from .ios_managed_app_protection import IosManagedAppProtection
				return IosManagedAppProtection.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .managed_app_data_storage_location import ManagedAppDataStorageLocation
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_browser_type import ManagedBrowserType
from .managed_app_pin_character_set import ManagedAppPinCharacterSet
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

