from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppProtection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	allowedDataStorageLocations: Optional[list[ManagedAppDataStorageLocation | str]] = Field(alias="allowedDataStorageLocations",default=None,)
	allowedInboundDataTransferSources: Optional[ManagedAppDataTransferLevel | str] = Field(alias="allowedInboundDataTransferSources",default=None,)
	allowedOutboundClipboardSharingLevel: Optional[ManagedAppClipboardSharingLevel | str] = Field(alias="allowedOutboundClipboardSharingLevel",default=None,)
	allowedOutboundDataTransferDestinations: Optional[ManagedAppDataTransferLevel | str] = Field(alias="allowedOutboundDataTransferDestinations",default=None,)
	contactSyncBlocked: Optional[bool] = Field(alias="contactSyncBlocked",default=None,)
	dataBackupBlocked: Optional[bool] = Field(alias="dataBackupBlocked",default=None,)
	deviceComplianceRequired: Optional[bool] = Field(alias="deviceComplianceRequired",default=None,)
	disableAppPinIfDevicePinIsSet: Optional[bool] = Field(alias="disableAppPinIfDevicePinIsSet",default=None,)
	fingerprintBlocked: Optional[bool] = Field(alias="fingerprintBlocked",default=None,)
	managedBrowser: Optional[ManagedBrowserType | str] = Field(alias="managedBrowser",default=None,)
	managedBrowserToOpenLinksRequired: Optional[bool] = Field(alias="managedBrowserToOpenLinksRequired",default=None,)
	maximumPinRetries: Optional[int] = Field(alias="maximumPinRetries",default=None,)
	minimumPinLength: Optional[int] = Field(alias="minimumPinLength",default=None,)
	minimumRequiredAppVersion: Optional[str] = Field(alias="minimumRequiredAppVersion",default=None,)
	minimumRequiredOsVersion: Optional[str] = Field(alias="minimumRequiredOsVersion",default=None,)
	minimumWarningAppVersion: Optional[str] = Field(alias="minimumWarningAppVersion",default=None,)
	minimumWarningOsVersion: Optional[str] = Field(alias="minimumWarningOsVersion",default=None,)
	organizationalCredentialsRequired: Optional[bool] = Field(alias="organizationalCredentialsRequired",default=None,)
	periodBeforePinReset: Optional[str] = Field(alias="periodBeforePinReset",default=None,)
	periodOfflineBeforeAccessCheck: Optional[str] = Field(alias="periodOfflineBeforeAccessCheck",default=None,)
	periodOfflineBeforeWipeIsEnforced: Optional[str] = Field(alias="periodOfflineBeforeWipeIsEnforced",default=None,)
	periodOnlineBeforeAccessCheck: Optional[str] = Field(alias="periodOnlineBeforeAccessCheck",default=None,)
	pinCharacterSet: Optional[ManagedAppPinCharacterSet | str] = Field(alias="pinCharacterSet",default=None,)
	pinRequired: Optional[bool] = Field(alias="pinRequired",default=None,)
	printBlocked: Optional[bool] = Field(alias="printBlocked",default=None,)
	saveAsBlocked: Optional[bool] = Field(alias="saveAsBlocked",default=None,)
	simplePinBlocked: Optional[bool] = Field(alias="simplePinBlocked",default=None,)

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
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .managed_app_data_storage_location import ManagedAppDataStorageLocation
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_browser_type import ManagedBrowserType
from .managed_app_pin_character_set import ManagedAppPinCharacterSet

