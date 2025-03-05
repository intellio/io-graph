from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidWorkProfileGeneralDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	passwordBlockFingerprintUnlock: Optional[bool] = Field(alias="passwordBlockFingerprintUnlock",default=None,)
	passwordBlockTrustAgents: Optional[bool] = Field(alias="passwordBlockTrustAgents",default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays",default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength",default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout",default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount",default=None,)
	passwordRequiredType: Optional[AndroidWorkProfileRequiredPasswordType | str] = Field(alias="passwordRequiredType",default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset",default=None,)
	securityRequireVerifyApps: Optional[bool] = Field(alias="securityRequireVerifyApps",default=None,)
	workProfileBlockAddingAccounts: Optional[bool] = Field(alias="workProfileBlockAddingAccounts",default=None,)
	workProfileBlockCamera: Optional[bool] = Field(alias="workProfileBlockCamera",default=None,)
	workProfileBlockCrossProfileCallerId: Optional[bool] = Field(alias="workProfileBlockCrossProfileCallerId",default=None,)
	workProfileBlockCrossProfileContactsSearch: Optional[bool] = Field(alias="workProfileBlockCrossProfileContactsSearch",default=None,)
	workProfileBlockCrossProfileCopyPaste: Optional[bool] = Field(alias="workProfileBlockCrossProfileCopyPaste",default=None,)
	workProfileBlockNotificationsWhileDeviceLocked: Optional[bool] = Field(alias="workProfileBlockNotificationsWhileDeviceLocked",default=None,)
	workProfileBlockScreenCapture: Optional[bool] = Field(alias="workProfileBlockScreenCapture",default=None,)
	workProfileBluetoothEnableContactSharing: Optional[bool] = Field(alias="workProfileBluetoothEnableContactSharing",default=None,)
	workProfileDataSharingType: Optional[AndroidWorkProfileCrossProfileDataSharingType | str] = Field(alias="workProfileDataSharingType",default=None,)
	workProfileDefaultAppPermissionPolicy: Optional[AndroidWorkProfileDefaultAppPermissionPolicyType | str] = Field(alias="workProfileDefaultAppPermissionPolicy",default=None,)
	workProfilePasswordBlockFingerprintUnlock: Optional[bool] = Field(alias="workProfilePasswordBlockFingerprintUnlock",default=None,)
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
	workProfilePasswordRequiredType: Optional[AndroidWorkProfileRequiredPasswordType | str] = Field(alias="workProfilePasswordRequiredType",default=None,)
	workProfilePasswordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="workProfilePasswordSignInFailureCountBeforeFactoryReset",default=None,)
	workProfileRequirePassword: Optional[bool] = Field(alias="workProfileRequirePassword",default=None,)

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

