from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows81CompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceCompliancePolicyAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceComplianceDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceComplianceDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	scheduledActionsForRule: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(alias="scheduledActionsForRule",default=None,)
	userStatuses: Optional[list[DeviceComplianceUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceComplianceUserOverview] = Field(alias="userStatusOverview",default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion",default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion",default=None,)
	passwordBlockSimple: Optional[bool] = Field(alias="passwordBlockSimple",default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays",default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount",default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength",default=None,)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeLock",default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount",default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired",default=None,)
	passwordRequiredType: Optional[RequiredPasswordType | str] = Field(alias="passwordRequiredType",default=None,)
	storageRequireEncryption: Optional[bool] = Field(alias="storageRequireEncryption",default=None,)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .required_password_type import RequiredPasswordType

