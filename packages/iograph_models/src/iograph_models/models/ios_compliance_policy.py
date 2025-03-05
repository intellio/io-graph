from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosCompliancePolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[DeviceCompliancePolicyAssignment]] = Field(default=None,alias="assignments",)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="deviceSettingStateSummaries",)
	deviceStatuses: Optional[list[DeviceComplianceDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceComplianceDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	scheduledActionsForRule: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(default=None,alias="scheduledActionsForRule",)
	userStatuses: Optional[list[DeviceComplianceUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusOverview: Optional[DeviceComplianceUserOverview] = Field(default=None,alias="userStatusOverview",)
	deviceThreatProtectionEnabled: Optional[bool] = Field(default=None,alias="deviceThreatProtectionEnabled",)
	deviceThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel] = Field(default=None,alias="deviceThreatProtectionRequiredSecurityLevel",)
	managedEmailProfileRequired: Optional[bool] = Field(default=None,alias="managedEmailProfileRequired",)
	osMaximumVersion: Optional[str] = Field(default=None,alias="osMaximumVersion",)
	osMinimumVersion: Optional[str] = Field(default=None,alias="osMinimumVersion",)
	passcodeBlockSimple: Optional[bool] = Field(default=None,alias="passcodeBlockSimple",)
	passcodeExpirationDays: Optional[int] = Field(default=None,alias="passcodeExpirationDays",)
	passcodeMinimumCharacterSetCount: Optional[int] = Field(default=None,alias="passcodeMinimumCharacterSetCount",)
	passcodeMinimumLength: Optional[int] = Field(default=None,alias="passcodeMinimumLength",)
	passcodeMinutesOfInactivityBeforeLock: Optional[int] = Field(default=None,alias="passcodeMinutesOfInactivityBeforeLock",)
	passcodePreviousPasscodeBlockCount: Optional[int] = Field(default=None,alias="passcodePreviousPasscodeBlockCount",)
	passcodeRequired: Optional[bool] = Field(default=None,alias="passcodeRequired",)
	passcodeRequiredType: Optional[RequiredPasswordType] = Field(default=None,alias="passcodeRequiredType",)
	securityBlockJailbrokenDevices: Optional[bool] = Field(default=None,alias="securityBlockJailbrokenDevices",)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .required_password_type import RequiredPasswordType

