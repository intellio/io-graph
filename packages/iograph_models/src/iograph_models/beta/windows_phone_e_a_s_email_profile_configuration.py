from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsPhoneEASEmailProfileConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsPhoneEASEmailProfileConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsPhoneEASEmailProfileConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode", default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition", default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	customDomainName: Optional[str] = Field(alias="customDomainName", default=None,)
	userDomainNameSource: Optional[DomainNameSource | str] = Field(alias="userDomainNameSource", default=None,)
	usernameAADSource: Optional[UsernameSource | str] = Field(alias="usernameAADSource", default=None,)
	usernameSource: Optional[UserEmailSource | str] = Field(alias="usernameSource", default=None,)
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	applyOnlyToWindowsPhone81: Optional[bool] = Field(alias="applyOnlyToWindowsPhone81", default=None,)
	durationOfEmailToSync: Optional[EmailSyncDuration | str] = Field(alias="durationOfEmailToSync", default=None,)
	emailAddressSource: Optional[UserEmailSource | str] = Field(alias="emailAddressSource", default=None,)
	emailSyncSchedule: Optional[EmailSyncSchedule | str] = Field(alias="emailSyncSchedule", default=None,)
	hostName: Optional[str] = Field(alias="hostName", default=None,)
	requireSsl: Optional[bool] = Field(alias="requireSsl", default=None,)
	syncCalendar: Optional[bool] = Field(alias="syncCalendar", default=None,)
	syncContacts: Optional[bool] = Field(alias="syncContacts", default=None,)
	syncTasks: Optional[bool] = Field(alias="syncTasks", default=None,)

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
from .domain_name_source import DomainNameSource
from .username_source import UsernameSource
from .user_email_source import UserEmailSource
from .email_sync_duration import EmailSyncDuration
from .email_sync_schedule import EmailSyncSchedule
