from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidWorkProfileGeneralDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[DeviceConfigurationAssignment] = Field(alias="assignments",)
	deviceSettingStateSummaries: list[SettingStateDeviceSummary] = Field(alias="deviceSettingStateSummaries",)
	deviceStatuses: list[DeviceConfigurationDeviceStatus] = Field(alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: list[DeviceConfigurationUserStatus] = Field(alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)
	passwordBlockFingerprintUnlock: Optional[bool] = Field(default=None,alias="passwordBlockFingerprintUnlock",)
	passwordBlockTrustAgents: Optional[bool] = Field(default=None,alias="passwordBlockTrustAgents",)
	passwordExpirationDays: Optional[int] = Field(default=None,alias="passwordExpirationDays",)
	passwordMinimumLength: Optional[int] = Field(default=None,alias="passwordMinimumLength",)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeScreenTimeout",)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="passwordPreviousPasswordBlockCount",)
	passwordRequiredType: Optional[AndroidWorkProfileRequiredPasswordType] = Field(default=None,alias="passwordRequiredType",)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(default=None,alias="passwordSignInFailureCountBeforeFactoryReset",)
	securityRequireVerifyApps: Optional[bool] = Field(default=None,alias="securityRequireVerifyApps",)
	workProfileBlockAddingAccounts: Optional[bool] = Field(default=None,alias="workProfileBlockAddingAccounts",)
	workProfileBlockCamera: Optional[bool] = Field(default=None,alias="workProfileBlockCamera",)
	workProfileBlockCrossProfileCallerId: Optional[bool] = Field(default=None,alias="workProfileBlockCrossProfileCallerId",)
	workProfileBlockCrossProfileContactsSearch: Optional[bool] = Field(default=None,alias="workProfileBlockCrossProfileContactsSearch",)
	workProfileBlockCrossProfileCopyPaste: Optional[bool] = Field(default=None,alias="workProfileBlockCrossProfileCopyPaste",)
	workProfileBlockNotificationsWhileDeviceLocked: Optional[bool] = Field(default=None,alias="workProfileBlockNotificationsWhileDeviceLocked",)
	workProfileBlockScreenCapture: Optional[bool] = Field(default=None,alias="workProfileBlockScreenCapture",)
	workProfileBluetoothEnableContactSharing: Optional[bool] = Field(default=None,alias="workProfileBluetoothEnableContactSharing",)
	workProfileDataSharingType: Optional[AndroidWorkProfileCrossProfileDataSharingType] = Field(default=None,alias="workProfileDataSharingType",)
	workProfileDefaultAppPermissionPolicy: Optional[AndroidWorkProfileDefaultAppPermissionPolicyType] = Field(default=None,alias="workProfileDefaultAppPermissionPolicy",)
	workProfilePasswordBlockFingerprintUnlock: Optional[bool] = Field(default=None,alias="workProfilePasswordBlockFingerprintUnlock",)
	workProfilePasswordBlockTrustAgents: Optional[bool] = Field(default=None,alias="workProfilePasswordBlockTrustAgents",)
	workProfilePasswordExpirationDays: Optional[int] = Field(default=None,alias="workProfilePasswordExpirationDays",)
	workProfilePasswordMinimumLength: Optional[int] = Field(default=None,alias="workProfilePasswordMinimumLength",)
	workProfilePasswordMinLetterCharacters: Optional[int] = Field(default=None,alias="workProfilePasswordMinLetterCharacters",)
	workProfilePasswordMinLowerCaseCharacters: Optional[int] = Field(default=None,alias="workProfilePasswordMinLowerCaseCharacters",)
	workProfilePasswordMinNonLetterCharacters: Optional[int] = Field(default=None,alias="workProfilePasswordMinNonLetterCharacters",)
	workProfilePasswordMinNumericCharacters: Optional[int] = Field(default=None,alias="workProfilePasswordMinNumericCharacters",)
	workProfilePasswordMinSymbolCharacters: Optional[int] = Field(default=None,alias="workProfilePasswordMinSymbolCharacters",)
	workProfilePasswordMinUpperCaseCharacters: Optional[int] = Field(default=None,alias="workProfilePasswordMinUpperCaseCharacters",)
	workProfilePasswordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(default=None,alias="workProfilePasswordMinutesOfInactivityBeforeScreenTimeout",)
	workProfilePasswordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="workProfilePasswordPreviousPasswordBlockCount",)
	workProfilePasswordRequiredType: Optional[AndroidWorkProfileRequiredPasswordType] = Field(default=None,alias="workProfilePasswordRequiredType",)
	workProfilePasswordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(default=None,alias="workProfilePasswordSignInFailureCountBeforeFactoryReset",)
	workProfileRequirePassword: Optional[bool] = Field(default=None,alias="workProfileRequirePassword",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType

