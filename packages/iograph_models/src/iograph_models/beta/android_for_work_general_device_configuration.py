from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkGeneralDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode",default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition",default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	allowedGoogleAccountDomains: Optional[list[str]] = Field(alias="allowedGoogleAccountDomains",default=None,)
	blockUnifiedPasswordForWorkProfile: Optional[bool] = Field(alias="blockUnifiedPasswordForWorkProfile",default=None,)
	passwordBlockFaceUnlock: Optional[bool] = Field(alias="passwordBlockFaceUnlock",default=None,)
	passwordBlockFingerprintUnlock: Optional[bool] = Field(alias="passwordBlockFingerprintUnlock",default=None,)
	passwordBlockIrisUnlock: Optional[bool] = Field(alias="passwordBlockIrisUnlock",default=None,)
	passwordBlockTrustAgents: Optional[bool] = Field(alias="passwordBlockTrustAgents",default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays",default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength",default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout",default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount",default=None,)
	passwordRequiredType: Optional[AndroidForWorkRequiredPasswordType | str] = Field(alias="passwordRequiredType",default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset",default=None,)
	requiredPasswordComplexity: Optional[AndroidRequiredPasswordComplexity | str] = Field(alias="requiredPasswordComplexity",default=None,)
	securityRequireVerifyApps: Optional[bool] = Field(alias="securityRequireVerifyApps",default=None,)
	vpnAlwaysOnPackageIdentifier: Optional[str] = Field(alias="vpnAlwaysOnPackageIdentifier",default=None,)
	vpnEnableAlwaysOnLockdownMode: Optional[bool] = Field(alias="vpnEnableAlwaysOnLockdownMode",default=None,)
	workProfileAccountUse: Optional[AndroidWorkProfileAccountUse | str] = Field(alias="workProfileAccountUse",default=None,)
	workProfileAllowWidgets: Optional[bool] = Field(alias="workProfileAllowWidgets",default=None,)
	workProfileBlockAddingAccounts: Optional[bool] = Field(alias="workProfileBlockAddingAccounts",default=None,)
	workProfileBlockCamera: Optional[bool] = Field(alias="workProfileBlockCamera",default=None,)
	workProfileBlockCrossProfileCallerId: Optional[bool] = Field(alias="workProfileBlockCrossProfileCallerId",default=None,)
	workProfileBlockCrossProfileContactsSearch: Optional[bool] = Field(alias="workProfileBlockCrossProfileContactsSearch",default=None,)
	workProfileBlockCrossProfileCopyPaste: Optional[bool] = Field(alias="workProfileBlockCrossProfileCopyPaste",default=None,)
	workProfileBlockNotificationsWhileDeviceLocked: Optional[bool] = Field(alias="workProfileBlockNotificationsWhileDeviceLocked",default=None,)
	workProfileBlockPersonalAppInstallsFromUnknownSources: Optional[bool] = Field(alias="workProfileBlockPersonalAppInstallsFromUnknownSources",default=None,)
	workProfileBlockScreenCapture: Optional[bool] = Field(alias="workProfileBlockScreenCapture",default=None,)
	workProfileBluetoothEnableContactSharing: Optional[bool] = Field(alias="workProfileBluetoothEnableContactSharing",default=None,)
	workProfileDataSharingType: Optional[AndroidForWorkCrossProfileDataSharingType | str] = Field(alias="workProfileDataSharingType",default=None,)
	workProfileDefaultAppPermissionPolicy: Optional[AndroidForWorkDefaultAppPermissionPolicyType | str] = Field(alias="workProfileDefaultAppPermissionPolicy",default=None,)
	workProfilePasswordBlockFaceUnlock: Optional[bool] = Field(alias="workProfilePasswordBlockFaceUnlock",default=None,)
	workProfilePasswordBlockFingerprintUnlock: Optional[bool] = Field(alias="workProfilePasswordBlockFingerprintUnlock",default=None,)
	workProfilePasswordBlockIrisUnlock: Optional[bool] = Field(alias="workProfilePasswordBlockIrisUnlock",default=None,)
	workProfilePasswordBlockTrustAgents: Optional[bool] = Field(alias="workProfilePasswordBlockTrustAgents",default=None,)
	workProfilePasswordExpirationDays: Optional[int] = Field(alias="workProfilePasswordExpirationDays",default=None,)
	workProfilePasswordMinimumLength: Optional[int] = Field(alias="workProfilePasswordMinimumLength",default=None,)
	workProfilePasswordMinLetterCharacters: Optional[int] = Field(alias="workProfilePasswordMinLetterCharacters",default=None,)
	workProfilePasswordMinLowerCaseCharacters: Optional[int] = Field(alias="workProfilePasswordMinLowerCaseCharacters",default=None,)
	workProfilePasswordMinNonLetterCharacters: Optional[int] = Field(alias="workProfilePasswordMinNonLetterCharacters",default=None,)
	workProfilePasswordMinNumericCharacters: Optional[int] = Field(alias="workProfilePasswordMinNumericCharacters",default=None,)
	workProfilePasswordMinSymbolCharacters: Optional[int] = Field(alias="workProfilePasswordMinSymbolCharacters",default=None,)
	workProfilePasswordMinUpperCaseCharacters: Optional[int] = Field(alias="workProfilePasswordMinUpperCaseCharacters",default=None,)
	workProfilePasswordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="workProfilePasswordMinutesOfInactivityBeforeScreenTimeout",default=None,)
	workProfilePasswordPreviousPasswordBlockCount: Optional[int] = Field(alias="workProfilePasswordPreviousPasswordBlockCount",default=None,)
	workProfilePasswordRequiredType: Optional[AndroidForWorkRequiredPasswordType | str] = Field(alias="workProfilePasswordRequiredType",default=None,)
	workProfilePasswordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="workProfilePasswordSignInFailureCountBeforeFactoryReset",default=None,)
	workProfileRequiredPasswordComplexity: Optional[AndroidRequiredPasswordComplexity | str] = Field(alias="workProfileRequiredPasswordComplexity",default=None,)
	workProfileRequirePassword: Optional[bool] = Field(alias="workProfileRequirePassword",default=None,)

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
from .android_for_work_required_password_type import AndroidForWorkRequiredPasswordType
from .android_required_password_complexity import AndroidRequiredPasswordComplexity
from .android_work_profile_account_use import AndroidWorkProfileAccountUse
from .android_for_work_cross_profile_data_sharing_type import AndroidForWorkCrossProfileDataSharingType
from .android_for_work_default_app_permission_policy_type import AndroidForWorkDefaultAppPermissionPolicyType
from .android_for_work_required_password_type import AndroidForWorkRequiredPasswordType
from .android_required_password_complexity import AndroidRequiredPasswordComplexity

