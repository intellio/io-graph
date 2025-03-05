from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedAppProtection(BaseModel):
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
	isAssigned: Optional[bool] = Field(alias="isAssigned",default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments",default=None,)
	customBrowserDisplayName: Optional[str] = Field(alias="customBrowserDisplayName",default=None,)
	customBrowserPackageId: Optional[str] = Field(alias="customBrowserPackageId",default=None,)
	deployedAppCount: Optional[int] = Field(alias="deployedAppCount",default=None,)
	disableAppEncryptionIfDeviceEncryptionIsEnabled: Optional[bool] = Field(alias="disableAppEncryptionIfDeviceEncryptionIsEnabled",default=None,)
	encryptAppData: Optional[bool] = Field(alias="encryptAppData",default=None,)
	minimumRequiredPatchVersion: Optional[str] = Field(alias="minimumRequiredPatchVersion",default=None,)
	minimumWarningPatchVersion: Optional[str] = Field(alias="minimumWarningPatchVersion",default=None,)
	screenCaptureBlocked: Optional[bool] = Field(alias="screenCaptureBlocked",default=None,)
	apps: Optional[list[ManagedMobileApp]] = Field(alias="apps",default=None,)
	deploymentSummary: Optional[ManagedAppPolicyDeploymentSummary] = Field(alias="deploymentSummary",default=None,)

from .managed_app_data_storage_location import ManagedAppDataStorageLocation
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_browser_type import ManagedBrowserType
from .managed_app_pin_character_set import ManagedAppPinCharacterSet
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .managed_mobile_app import ManagedMobileApp
from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary

