from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidForWorkCompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidForWorkCompliancePolicy"] = Field(alias="@odata.type", default="#microsoft.graph.androidForWorkCompliancePolicy")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceCompliancePolicyAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceComplianceDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceComplianceDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	scheduledActionsForRule: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(alias="scheduledActionsForRule", default=None,)
	userStatuses: Optional[list[DeviceComplianceUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceComplianceUserOverview] = Field(alias="userStatusOverview", default=None,)
	deviceThreatProtectionEnabled: Optional[bool] = Field(alias="deviceThreatProtectionEnabled", default=None,)
	deviceThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel | str] = Field(alias="deviceThreatProtectionRequiredSecurityLevel", default=None,)
	minAndroidSecurityPatchLevel: Optional[str] = Field(alias="minAndroidSecurityPatchLevel", default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion", default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeLock", default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount", default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired", default=None,)
	passwordRequiredType: Optional[AndroidRequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset", default=None,)
	requiredPasswordComplexity: Optional[AndroidRequiredPasswordComplexity | str] = Field(alias="requiredPasswordComplexity", default=None,)
	securityBlockJailbrokenDevices: Optional[bool] = Field(alias="securityBlockJailbrokenDevices", default=None,)
	securityDisableUsbDebugging: Optional[bool] = Field(alias="securityDisableUsbDebugging", default=None,)
	securityPreventInstallAppsFromUnknownSources: Optional[bool] = Field(alias="securityPreventInstallAppsFromUnknownSources", default=None,)
	securityRequireCompanyPortalAppIntegrity: Optional[bool] = Field(alias="securityRequireCompanyPortalAppIntegrity", default=None,)
	securityRequiredAndroidSafetyNetEvaluationType: Optional[AndroidSafetyNetEvaluationType | str] = Field(alias="securityRequiredAndroidSafetyNetEvaluationType", default=None,)
	securityRequireGooglePlayServices: Optional[bool] = Field(alias="securityRequireGooglePlayServices", default=None,)
	securityRequireSafetyNetAttestationBasicIntegrity: Optional[bool] = Field(alias="securityRequireSafetyNetAttestationBasicIntegrity", default=None,)
	securityRequireSafetyNetAttestationCertifiedDevice: Optional[bool] = Field(alias="securityRequireSafetyNetAttestationCertifiedDevice", default=None,)
	securityRequireUpToDateSecurityProviders: Optional[bool] = Field(alias="securityRequireUpToDateSecurityProviders", default=None,)
	securityRequireVerifyApps: Optional[bool] = Field(alias="securityRequireVerifyApps", default=None,)
	storageRequireEncryption: Optional[bool] = Field(alias="storageRequireEncryption", default=None,)
	workProfileInactiveBeforeScreenLockInMinutes: Optional[int] = Field(alias="workProfileInactiveBeforeScreenLockInMinutes", default=None,)
	workProfilePasswordExpirationInDays: Optional[int] = Field(alias="workProfilePasswordExpirationInDays", default=None,)
	workProfilePasswordMinimumLength: Optional[int] = Field(alias="workProfilePasswordMinimumLength", default=None,)
	workProfilePasswordRequiredType: Optional[AndroidForWorkRequiredPasswordType | str] = Field(alias="workProfilePasswordRequiredType", default=None,)
	workProfilePreviousPasswordBlockCount: Optional[int] = Field(alias="workProfilePreviousPasswordBlockCount", default=None,)
	workProfileRequiredPasswordComplexity: Optional[AndroidRequiredPasswordComplexity | str] = Field(alias="workProfileRequiredPasswordComplexity", default=None,)
	workProfileRequirePassword: Optional[bool] = Field(alias="workProfileRequirePassword", default=None,)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .android_required_password_type import AndroidRequiredPasswordType
from .android_required_password_complexity import AndroidRequiredPasswordComplexity
from .android_safety_net_evaluation_type import AndroidSafetyNetEvaluationType
from .android_for_work_required_password_type import AndroidForWorkRequiredPasswordType
