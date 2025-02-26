from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidCompliancePolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[DeviceCompliancePolicyAssignment] = Field(alias="assignments",)
	deviceSettingStateSummaries: list[SettingStateDeviceSummary] = Field(alias="deviceSettingStateSummaries",)
	deviceStatuses: list[DeviceComplianceDeviceStatus] = Field(alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceComplianceDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	scheduledActionsForRule: list[DeviceComplianceScheduledActionForRule] = Field(alias="scheduledActionsForRule",)
	userStatuses: list[DeviceComplianceUserStatus] = Field(alias="userStatuses",)
	userStatusOverview: Optional[DeviceComplianceUserOverview] = Field(default=None,alias="userStatusOverview",)
	deviceThreatProtectionEnabled: Optional[bool] = Field(default=None,alias="deviceThreatProtectionEnabled",)
	deviceThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel] = Field(default=None,alias="deviceThreatProtectionRequiredSecurityLevel",)
	minAndroidSecurityPatchLevel: Optional[str] = Field(default=None,alias="minAndroidSecurityPatchLevel",)
	osMaximumVersion: Optional[str] = Field(default=None,alias="osMaximumVersion",)
	osMinimumVersion: Optional[str] = Field(default=None,alias="osMinimumVersion",)
	passwordExpirationDays: Optional[int] = Field(default=None,alias="passwordExpirationDays",)
	passwordMinimumLength: Optional[int] = Field(default=None,alias="passwordMinimumLength",)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeLock",)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="passwordPreviousPasswordBlockCount",)
	passwordRequired: Optional[bool] = Field(default=None,alias="passwordRequired",)
	passwordRequiredType: Optional[AndroidRequiredPasswordType] = Field(default=None,alias="passwordRequiredType",)
	securityBlockJailbrokenDevices: Optional[bool] = Field(default=None,alias="securityBlockJailbrokenDevices",)
	securityDisableUsbDebugging: Optional[bool] = Field(default=None,alias="securityDisableUsbDebugging",)
	securityPreventInstallAppsFromUnknownSources: Optional[bool] = Field(default=None,alias="securityPreventInstallAppsFromUnknownSources",)
	securityRequireCompanyPortalAppIntegrity: Optional[bool] = Field(default=None,alias="securityRequireCompanyPortalAppIntegrity",)
	securityRequireGooglePlayServices: Optional[bool] = Field(default=None,alias="securityRequireGooglePlayServices",)
	securityRequireSafetyNetAttestationBasicIntegrity: Optional[bool] = Field(default=None,alias="securityRequireSafetyNetAttestationBasicIntegrity",)
	securityRequireSafetyNetAttestationCertifiedDevice: Optional[bool] = Field(default=None,alias="securityRequireSafetyNetAttestationCertifiedDevice",)
	securityRequireUpToDateSecurityProviders: Optional[bool] = Field(default=None,alias="securityRequireUpToDateSecurityProviders",)
	securityRequireVerifyApps: Optional[bool] = Field(default=None,alias="securityRequireVerifyApps",)
	storageRequireEncryption: Optional[bool] = Field(default=None,alias="storageRequireEncryption",)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .android_required_password_type import AndroidRequiredPasswordType

