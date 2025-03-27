from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSCompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSCompliancePolicy"] = Field(alias="@odata.type", default="#microsoft.graph.macOSCompliancePolicy")
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
	advancedThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel | str] = Field(alias="advancedThreatProtectionRequiredSecurityLevel", default=None,)
	deviceThreatProtectionEnabled: Optional[bool] = Field(alias="deviceThreatProtectionEnabled", default=None,)
	deviceThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel | str] = Field(alias="deviceThreatProtectionRequiredSecurityLevel", default=None,)
	firewallBlockAllIncoming: Optional[bool] = Field(alias="firewallBlockAllIncoming", default=None,)
	firewallEnabled: Optional[bool] = Field(alias="firewallEnabled", default=None,)
	firewallEnableStealthMode: Optional[bool] = Field(alias="firewallEnableStealthMode", default=None,)
	gatekeeperAllowedAppSource: Optional[MacOSGatekeeperAppSources | str] = Field(alias="gatekeeperAllowedAppSource", default=None,)
	osMaximumBuildVersion: Optional[str] = Field(alias="osMaximumBuildVersion", default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion", default=None,)
	osMinimumBuildVersion: Optional[str] = Field(alias="osMinimumBuildVersion", default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion", default=None,)
	passwordBlockSimple: Optional[bool] = Field(alias="passwordBlockSimple", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeLock", default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount", default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired", default=None,)
	passwordRequiredType: Optional[RequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	storageRequireEncryption: Optional[bool] = Field(alias="storageRequireEncryption", default=None,)
	systemIntegrityProtectionEnabled: Optional[bool] = Field(alias="systemIntegrityProtectionEnabled", default=None,)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .mac_o_s_gatekeeper_app_sources import MacOSGatekeeperAppSources
from .required_password_type import RequiredPasswordType

