from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IosManagedAppProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosManagedAppProtection"] = Field(alias="@odata.type", default="#microsoft.graph.iosManagedAppProtection")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	allowedDataIngestionLocations: Optional[list[ManagedAppDataIngestionLocation | str]] = Field(alias="allowedDataIngestionLocations", default=None,)
	allowedDataStorageLocations: Optional[list[ManagedAppDataStorageLocation | str]] = Field(alias="allowedDataStorageLocations", default=None,)
	allowedInboundDataTransferSources: Optional[ManagedAppDataTransferLevel | str] = Field(alias="allowedInboundDataTransferSources", default=None,)
	allowedOutboundClipboardSharingExceptionLength: Optional[int] = Field(alias="allowedOutboundClipboardSharingExceptionLength", default=None,)
	allowedOutboundClipboardSharingLevel: Optional[ManagedAppClipboardSharingLevel | str] = Field(alias="allowedOutboundClipboardSharingLevel", default=None,)
	allowedOutboundDataTransferDestinations: Optional[ManagedAppDataTransferLevel | str] = Field(alias="allowedOutboundDataTransferDestinations", default=None,)
	appActionIfDeviceComplianceRequired: Optional[ManagedAppRemediationAction | str] = Field(alias="appActionIfDeviceComplianceRequired", default=None,)
	appActionIfMaximumPinRetriesExceeded: Optional[ManagedAppRemediationAction | str] = Field(alias="appActionIfMaximumPinRetriesExceeded", default=None,)
	appActionIfUnableToAuthenticateUser: Optional[ManagedAppRemediationAction | str] = Field(alias="appActionIfUnableToAuthenticateUser", default=None,)
	blockDataIngestionIntoOrganizationDocuments: Optional[bool] = Field(alias="blockDataIngestionIntoOrganizationDocuments", default=None,)
	contactSyncBlocked: Optional[bool] = Field(alias="contactSyncBlocked", default=None,)
	dataBackupBlocked: Optional[bool] = Field(alias="dataBackupBlocked", default=None,)
	deviceComplianceRequired: Optional[bool] = Field(alias="deviceComplianceRequired", default=None,)
	dialerRestrictionLevel: Optional[ManagedAppPhoneNumberRedirectLevel | str] = Field(alias="dialerRestrictionLevel", default=None,)
	disableAppPinIfDevicePinIsSet: Optional[bool] = Field(alias="disableAppPinIfDevicePinIsSet", default=None,)
	fingerprintBlocked: Optional[bool] = Field(alias="fingerprintBlocked", default=None,)
	gracePeriodToBlockAppsDuringOffClockHours: Optional[str] = Field(alias="gracePeriodToBlockAppsDuringOffClockHours", default=None,)
	managedBrowser: Optional[ManagedBrowserType | str] = Field(alias="managedBrowser", default=None,)
	managedBrowserToOpenLinksRequired: Optional[bool] = Field(alias="managedBrowserToOpenLinksRequired", default=None,)
	maximumAllowedDeviceThreatLevel: Optional[ManagedAppDeviceThreatLevel | str] = Field(alias="maximumAllowedDeviceThreatLevel", default=None,)
	maximumPinRetries: Optional[int] = Field(alias="maximumPinRetries", default=None,)
	maximumRequiredOsVersion: Optional[str] = Field(alias="maximumRequiredOsVersion", default=None,)
	maximumWarningOsVersion: Optional[str] = Field(alias="maximumWarningOsVersion", default=None,)
	maximumWipeOsVersion: Optional[str] = Field(alias="maximumWipeOsVersion", default=None,)
	minimumPinLength: Optional[int] = Field(alias="minimumPinLength", default=None,)
	minimumRequiredAppVersion: Optional[str] = Field(alias="minimumRequiredAppVersion", default=None,)
	minimumRequiredOsVersion: Optional[str] = Field(alias="minimumRequiredOsVersion", default=None,)
	minimumWarningAppVersion: Optional[str] = Field(alias="minimumWarningAppVersion", default=None,)
	minimumWarningOsVersion: Optional[str] = Field(alias="minimumWarningOsVersion", default=None,)
	minimumWipeAppVersion: Optional[str] = Field(alias="minimumWipeAppVersion", default=None,)
	minimumWipeOsVersion: Optional[str] = Field(alias="minimumWipeOsVersion", default=None,)
	mobileThreatDefensePartnerPriority: Optional[MobileThreatDefensePartnerPriority | str] = Field(alias="mobileThreatDefensePartnerPriority", default=None,)
	mobileThreatDefenseRemediationAction: Optional[ManagedAppRemediationAction | str] = Field(alias="mobileThreatDefenseRemediationAction", default=None,)
	notificationRestriction: Optional[ManagedAppNotificationRestriction | str] = Field(alias="notificationRestriction", default=None,)
	organizationalCredentialsRequired: Optional[bool] = Field(alias="organizationalCredentialsRequired", default=None,)
	periodBeforePinReset: Optional[str] = Field(alias="periodBeforePinReset", default=None,)
	periodOfflineBeforeAccessCheck: Optional[str] = Field(alias="periodOfflineBeforeAccessCheck", default=None,)
	periodOfflineBeforeWipeIsEnforced: Optional[str] = Field(alias="periodOfflineBeforeWipeIsEnforced", default=None,)
	periodOnlineBeforeAccessCheck: Optional[str] = Field(alias="periodOnlineBeforeAccessCheck", default=None,)
	pinCharacterSet: Optional[ManagedAppPinCharacterSet | str] = Field(alias="pinCharacterSet", default=None,)
	pinRequired: Optional[bool] = Field(alias="pinRequired", default=None,)
	pinRequiredInsteadOfBiometricTimeout: Optional[str] = Field(alias="pinRequiredInsteadOfBiometricTimeout", default=None,)
	previousPinBlockCount: Optional[int] = Field(alias="previousPinBlockCount", default=None,)
	printBlocked: Optional[bool] = Field(alias="printBlocked", default=None,)
	protectedMessagingRedirectAppType: Optional[MessagingRedirectAppType | str] = Field(alias="protectedMessagingRedirectAppType", default=None,)
	saveAsBlocked: Optional[bool] = Field(alias="saveAsBlocked", default=None,)
	simplePinBlocked: Optional[bool] = Field(alias="simplePinBlocked", default=None,)
	appGroupType: Optional[TargetedManagedAppGroupType | str] = Field(alias="appGroupType", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	targetedAppManagementLevels: Optional[AppManagementLevel | str] = Field(alias="targetedAppManagementLevels", default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments", default=None,)
	allowedIosDeviceModels: Optional[str] = Field(alias="allowedIosDeviceModels", default=None,)
	allowWidgetContentSync: Optional[bool] = Field(alias="allowWidgetContentSync", default=None,)
	appActionIfAccountIsClockedOut: Optional[ManagedAppRemediationAction | str] = Field(alias="appActionIfAccountIsClockedOut", default=None,)
	appActionIfIosDeviceModelNotAllowed: Optional[ManagedAppRemediationAction | str] = Field(alias="appActionIfIosDeviceModelNotAllowed", default=None,)
	appDataEncryptionType: Optional[ManagedAppDataEncryptionType | str] = Field(alias="appDataEncryptionType", default=None,)
	customBrowserProtocol: Optional[str] = Field(alias="customBrowserProtocol", default=None,)
	customDialerAppProtocol: Optional[str] = Field(alias="customDialerAppProtocol", default=None,)
	deployedAppCount: Optional[int] = Field(alias="deployedAppCount", default=None,)
	disableProtectionOfManagedOutboundOpenInData: Optional[bool] = Field(alias="disableProtectionOfManagedOutboundOpenInData", default=None,)
	exemptedAppProtocols: Optional[list[KeyValuePair]] = Field(alias="exemptedAppProtocols", default=None,)
	exemptedUniversalLinks: Optional[list[str]] = Field(alias="exemptedUniversalLinks", default=None,)
	faceIdBlocked: Optional[bool] = Field(alias="faceIdBlocked", default=None,)
	filterOpenInToOnlyManagedApps: Optional[bool] = Field(alias="filterOpenInToOnlyManagedApps", default=None,)
	managedUniversalLinks: Optional[list[str]] = Field(alias="managedUniversalLinks", default=None,)
	messagingRedirectAppUrlScheme: Optional[str] = Field(alias="messagingRedirectAppUrlScheme", default=None,)
	minimumRequiredSdkVersion: Optional[str] = Field(alias="minimumRequiredSdkVersion", default=None,)
	minimumWarningSdkVersion: Optional[str] = Field(alias="minimumWarningSdkVersion", default=None,)
	minimumWipeSdkVersion: Optional[str] = Field(alias="minimumWipeSdkVersion", default=None,)
	protectInboundDataFromUnknownSources: Optional[bool] = Field(alias="protectInboundDataFromUnknownSources", default=None,)
	thirdPartyKeyboardsBlocked: Optional[bool] = Field(alias="thirdPartyKeyboardsBlocked", default=None,)
	apps: Optional[list[ManagedMobileApp]] = Field(alias="apps", default=None,)
	deploymentSummary: Optional[ManagedAppPolicyDeploymentSummary] = Field(alias="deploymentSummary", default=None,)

from .managed_app_data_ingestion_location import ManagedAppDataIngestionLocation
from .managed_app_data_storage_location import ManagedAppDataStorageLocation
from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
from .managed_app_remediation_action import ManagedAppRemediationAction
from .managed_app_phone_number_redirect_level import ManagedAppPhoneNumberRedirectLevel
from .managed_browser_type import ManagedBrowserType
from .managed_app_device_threat_level import ManagedAppDeviceThreatLevel
from .mobile_threat_defense_partner_priority import MobileThreatDefensePartnerPriority
from .managed_app_notification_restriction import ManagedAppNotificationRestriction
from .managed_app_pin_character_set import ManagedAppPinCharacterSet
from .messaging_redirect_app_type import MessagingRedirectAppType
from .targeted_managed_app_group_type import TargetedManagedAppGroupType
from .app_management_level import AppManagementLevel
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
from .key_value_pair import KeyValuePair
from .managed_mobile_app import ManagedMobileApp
from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
