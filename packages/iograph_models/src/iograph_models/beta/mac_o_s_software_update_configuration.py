from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSSoftwareUpdateConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode",default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition",default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	allOtherUpdateBehavior: Optional[MacOSSoftwareUpdateBehavior | str] = Field(alias="allOtherUpdateBehavior",default=None,)
	configDataUpdateBehavior: Optional[MacOSSoftwareUpdateBehavior | str] = Field(alias="configDataUpdateBehavior",default=None,)
	criticalUpdateBehavior: Optional[MacOSSoftwareUpdateBehavior | str] = Field(alias="criticalUpdateBehavior",default=None,)
	customUpdateTimeWindows: Optional[list[CustomUpdateTimeWindow]] = Field(alias="customUpdateTimeWindows",default=None,)
	firmwareUpdateBehavior: Optional[MacOSSoftwareUpdateBehavior | str] = Field(alias="firmwareUpdateBehavior",default=None,)
	maxUserDeferralsCount: Optional[int] = Field(alias="maxUserDeferralsCount",default=None,)
	priority: Optional[MacOSPriority | str] = Field(alias="priority",default=None,)
	updateScheduleType: Optional[MacOSSoftwareUpdateScheduleType | str] = Field(alias="updateScheduleType",default=None,)
	updateTimeWindowUtcOffsetInMinutes: Optional[int] = Field(alias="updateTimeWindowUtcOffsetInMinutes",default=None,)

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
from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
from .custom_update_time_window import CustomUpdateTimeWindow
from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
from .mac_o_s_priority import MacOSPriority
from .mac_o_s_software_update_schedule_type import MacOSSoftwareUpdateScheduleType

