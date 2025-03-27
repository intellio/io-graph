from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10CompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10CompliancePolicy"] = Field(alias="@odata.type", default="#microsoft.graph.windows10CompliancePolicy")
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
	activeFirewallRequired: Optional[bool] = Field(alias="activeFirewallRequired", default=None,)
	antiSpywareRequired: Optional[bool] = Field(alias="antiSpywareRequired", default=None,)
	antivirusRequired: Optional[bool] = Field(alias="antivirusRequired", default=None,)
	bitLockerEnabled: Optional[bool] = Field(alias="bitLockerEnabled", default=None,)
	codeIntegrityEnabled: Optional[bool] = Field(alias="codeIntegrityEnabled", default=None,)
	configurationManagerComplianceRequired: Optional[bool] = Field(alias="configurationManagerComplianceRequired", default=None,)
	defenderEnabled: Optional[bool] = Field(alias="defenderEnabled", default=None,)
	defenderVersion: Optional[str] = Field(alias="defenderVersion", default=None,)
	deviceCompliancePolicyScript: Optional[DeviceCompliancePolicyScript] = Field(alias="deviceCompliancePolicyScript", default=None,)
	deviceThreatProtectionEnabled: Optional[bool] = Field(alias="deviceThreatProtectionEnabled", default=None,)
	deviceThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel | str] = Field(alias="deviceThreatProtectionRequiredSecurityLevel", default=None,)
	earlyLaunchAntiMalwareDriverEnabled: Optional[bool] = Field(alias="earlyLaunchAntiMalwareDriverEnabled", default=None,)
	firmwareProtectionEnabled: Optional[bool] = Field(alias="firmwareProtectionEnabled", default=None,)
	kernelDmaProtectionEnabled: Optional[bool] = Field(alias="kernelDmaProtectionEnabled", default=None,)
	memoryIntegrityEnabled: Optional[bool] = Field(alias="memoryIntegrityEnabled", default=None,)
	mobileOsMaximumVersion: Optional[str] = Field(alias="mobileOsMaximumVersion", default=None,)
	mobileOsMinimumVersion: Optional[str] = Field(alias="mobileOsMinimumVersion", default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion", default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion", default=None,)
	passwordBlockSimple: Optional[bool] = Field(alias="passwordBlockSimple", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeLock", default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount", default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired", default=None,)
	passwordRequiredToUnlockFromIdle: Optional[bool] = Field(alias="passwordRequiredToUnlockFromIdle", default=None,)
	passwordRequiredType: Optional[RequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	requireHealthyDeviceReport: Optional[bool] = Field(alias="requireHealthyDeviceReport", default=None,)
	rtpEnabled: Optional[bool] = Field(alias="rtpEnabled", default=None,)
	secureBootEnabled: Optional[bool] = Field(alias="secureBootEnabled", default=None,)
	signatureOutOfDate: Optional[bool] = Field(alias="signatureOutOfDate", default=None,)
	storageRequireEncryption: Optional[bool] = Field(alias="storageRequireEncryption", default=None,)
	tpmRequired: Optional[bool] = Field(alias="tpmRequired", default=None,)
	validOperatingSystemBuildRanges: Optional[list[OperatingSystemVersionRange]] = Field(alias="validOperatingSystemBuildRanges", default=None,)
	virtualizationBasedSecurityEnabled: Optional[bool] = Field(alias="virtualizationBasedSecurityEnabled", default=None,)
	wslDistributions: Optional[list[WslDistributionConfiguration]] = Field(alias="wslDistributions", default=None,)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_compliance_policy_script import DeviceCompliancePolicyScript
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .required_password_type import RequiredPasswordType
from .operating_system_version_range import OperatingSystemVersionRange
from .wsl_distribution_configuration import WslDistributionConfiguration

