from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosCompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosCompliancePolicy"] = Field(alias="@odata.type", default="#microsoft.graph.iosCompliancePolicy")
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
	managedEmailProfileRequired: Optional[bool] = Field(alias="managedEmailProfileRequired", default=None,)
	osMaximumBuildVersion: Optional[str] = Field(alias="osMaximumBuildVersion", default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion", default=None,)
	osMinimumBuildVersion: Optional[str] = Field(alias="osMinimumBuildVersion", default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion", default=None,)
	passcodeBlockSimple: Optional[bool] = Field(alias="passcodeBlockSimple", default=None,)
	passcodeExpirationDays: Optional[int] = Field(alias="passcodeExpirationDays", default=None,)
	passcodeMinimumCharacterSetCount: Optional[int] = Field(alias="passcodeMinimumCharacterSetCount", default=None,)
	passcodeMinimumLength: Optional[int] = Field(alias="passcodeMinimumLength", default=None,)
	passcodeMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passcodeMinutesOfInactivityBeforeLock", default=None,)
	passcodeMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passcodeMinutesOfInactivityBeforeScreenTimeout", default=None,)
	passcodePreviousPasscodeBlockCount: Optional[int] = Field(alias="passcodePreviousPasscodeBlockCount", default=None,)
	passcodeRequired: Optional[bool] = Field(alias="passcodeRequired", default=None,)
	passcodeRequiredType: Optional[RequiredPasswordType | str] = Field(alias="passcodeRequiredType", default=None,)
	restrictedApps: Optional[list[Annotated[Union[AppleAppListItem],Field(discriminator="odata_type")]]] = Field(alias="restrictedApps", default=None,)
	securityBlockJailbrokenDevices: Optional[bool] = Field(alias="securityBlockJailbrokenDevices", default=None,)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .required_password_type import RequiredPasswordType
from .apple_app_list_item import AppleAppListItem

