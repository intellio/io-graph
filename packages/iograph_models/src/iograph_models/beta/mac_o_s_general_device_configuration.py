from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSGeneralDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSGeneralDeviceConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.macOSGeneralDeviceConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode", default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition", default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	activationLockWhenSupervisedAllowed: Optional[bool] = Field(alias="activationLockWhenSupervisedAllowed", default=None,)
	addingGameCenterFriendsBlocked: Optional[bool] = Field(alias="addingGameCenterFriendsBlocked", default=None,)
	airDropBlocked: Optional[bool] = Field(alias="airDropBlocked", default=None,)
	appleWatchBlockAutoUnlock: Optional[bool] = Field(alias="appleWatchBlockAutoUnlock", default=None,)
	cameraBlocked: Optional[bool] = Field(alias="cameraBlocked", default=None,)
	classroomAppBlockRemoteScreenObservation: Optional[bool] = Field(alias="classroomAppBlockRemoteScreenObservation", default=None,)
	classroomAppForceUnpromptedScreenObservation: Optional[bool] = Field(alias="classroomAppForceUnpromptedScreenObservation", default=None,)
	classroomForceAutomaticallyJoinClasses: Optional[bool] = Field(alias="classroomForceAutomaticallyJoinClasses", default=None,)
	classroomForceRequestPermissionToLeaveClasses: Optional[bool] = Field(alias="classroomForceRequestPermissionToLeaveClasses", default=None,)
	classroomForceUnpromptedAppAndDeviceLock: Optional[bool] = Field(alias="classroomForceUnpromptedAppAndDeviceLock", default=None,)
	compliantAppListType: Optional[AppListType | str] = Field(alias="compliantAppListType", default=None,)
	compliantAppsList: Optional[list[Annotated[Union[AppleAppListItem],Field(discriminator="odata_type")]]] = Field(alias="compliantAppsList", default=None,)
	contentCachingBlocked: Optional[bool] = Field(alias="contentCachingBlocked", default=None,)
	definitionLookupBlocked: Optional[bool] = Field(alias="definitionLookupBlocked", default=None,)
	emailInDomainSuffixes: Optional[list[str]] = Field(alias="emailInDomainSuffixes", default=None,)
	eraseContentAndSettingsBlocked: Optional[bool] = Field(alias="eraseContentAndSettingsBlocked", default=None,)
	gameCenterBlocked: Optional[bool] = Field(alias="gameCenterBlocked", default=None,)
	iCloudBlockActivityContinuation: Optional[bool] = Field(alias="iCloudBlockActivityContinuation", default=None,)
	iCloudBlockAddressBook: Optional[bool] = Field(alias="iCloudBlockAddressBook", default=None,)
	iCloudBlockBookmarks: Optional[bool] = Field(alias="iCloudBlockBookmarks", default=None,)
	iCloudBlockCalendar: Optional[bool] = Field(alias="iCloudBlockCalendar", default=None,)
	iCloudBlockDocumentSync: Optional[bool] = Field(alias="iCloudBlockDocumentSync", default=None,)
	iCloudBlockMail: Optional[bool] = Field(alias="iCloudBlockMail", default=None,)
	iCloudBlockNotes: Optional[bool] = Field(alias="iCloudBlockNotes", default=None,)
	iCloudBlockPhotoLibrary: Optional[bool] = Field(alias="iCloudBlockPhotoLibrary", default=None,)
	iCloudBlockReminders: Optional[bool] = Field(alias="iCloudBlockReminders", default=None,)
	iCloudDesktopAndDocumentsBlocked: Optional[bool] = Field(alias="iCloudDesktopAndDocumentsBlocked", default=None,)
	iCloudPrivateRelayBlocked: Optional[bool] = Field(alias="iCloudPrivateRelayBlocked", default=None,)
	iTunesBlockFileSharing: Optional[bool] = Field(alias="iTunesBlockFileSharing", default=None,)
	iTunesBlockMusicService: Optional[bool] = Field(alias="iTunesBlockMusicService", default=None,)
	keyboardBlockDictation: Optional[bool] = Field(alias="keyboardBlockDictation", default=None,)
	keychainBlockCloudSync: Optional[bool] = Field(alias="keychainBlockCloudSync", default=None,)
	multiplayerGamingBlocked: Optional[bool] = Field(alias="multiplayerGamingBlocked", default=None,)
	passwordBlockAirDropSharing: Optional[bool] = Field(alias="passwordBlockAirDropSharing", default=None,)
	passwordBlockAutoFill: Optional[bool] = Field(alias="passwordBlockAutoFill", default=None,)
	passwordBlockFingerprintUnlock: Optional[bool] = Field(alias="passwordBlockFingerprintUnlock", default=None,)
	passwordBlockModification: Optional[bool] = Field(alias="passwordBlockModification", default=None,)
	passwordBlockProximityRequests: Optional[bool] = Field(alias="passwordBlockProximityRequests", default=None,)
	passwordBlockSimple: Optional[bool] = Field(alias="passwordBlockSimple", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMaximumAttemptCount: Optional[int] = Field(alias="passwordMaximumAttemptCount", default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeLock", default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout", default=None,)
	passwordMinutesUntilFailedLoginReset: Optional[int] = Field(alias="passwordMinutesUntilFailedLoginReset", default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount", default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired", default=None,)
	passwordRequiredType: Optional[RequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	privacyAccessControls: Optional[list[MacOSPrivacyAccessControlItem]] = Field(alias="privacyAccessControls", default=None,)
	safariBlockAutofill: Optional[bool] = Field(alias="safariBlockAutofill", default=None,)
	screenCaptureBlocked: Optional[bool] = Field(alias="screenCaptureBlocked", default=None,)
	softwareUpdateMajorOSDeferredInstallDelayInDays: Optional[int] = Field(alias="softwareUpdateMajorOSDeferredInstallDelayInDays", default=None,)
	softwareUpdateMinorOSDeferredInstallDelayInDays: Optional[int] = Field(alias="softwareUpdateMinorOSDeferredInstallDelayInDays", default=None,)
	softwareUpdateNonOSDeferredInstallDelayInDays: Optional[int] = Field(alias="softwareUpdateNonOSDeferredInstallDelayInDays", default=None,)
	softwareUpdatesEnforcedDelayInDays: Optional[int] = Field(alias="softwareUpdatesEnforcedDelayInDays", default=None,)
	spotlightBlockInternetResults: Optional[bool] = Field(alias="spotlightBlockInternetResults", default=None,)
	touchIdTimeoutInHours: Optional[int] = Field(alias="touchIdTimeoutInHours", default=None,)
	updateDelayPolicy: Optional[MacOSSoftwareUpdateDelayPolicy | str] = Field(alias="updateDelayPolicy", default=None,)
	wallpaperModificationBlocked: Optional[bool] = Field(alias="wallpaperModificationBlocked", default=None,)

from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .app_list_type import AppListType
from .apple_app_list_item import AppleAppListItem
from .required_password_type import RequiredPasswordType
from .mac_o_s_privacy_access_control_item import MacOSPrivacyAccessControlItem
from .mac_o_s_software_update_delay_policy import MacOSSoftwareUpdateDelayPolicy
