from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsKioskConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskConfiguration")
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
	edgeKioskEnablePublicBrowsing: Optional[bool] = Field(alias="edgeKioskEnablePublicBrowsing", default=None,)
	kioskBrowserBlockedUrlExceptions: Optional[list[str]] = Field(alias="kioskBrowserBlockedUrlExceptions", default=None,)
	kioskBrowserBlockedURLs: Optional[list[str]] = Field(alias="kioskBrowserBlockedURLs", default=None,)
	kioskBrowserDefaultUrl: Optional[str] = Field(alias="kioskBrowserDefaultUrl", default=None,)
	kioskBrowserEnableEndSessionButton: Optional[bool] = Field(alias="kioskBrowserEnableEndSessionButton", default=None,)
	kioskBrowserEnableHomeButton: Optional[bool] = Field(alias="kioskBrowserEnableHomeButton", default=None,)
	kioskBrowserEnableNavigationButtons: Optional[bool] = Field(alias="kioskBrowserEnableNavigationButtons", default=None,)
	kioskBrowserRestartOnIdleTimeInMinutes: Optional[int] = Field(alias="kioskBrowserRestartOnIdleTimeInMinutes", default=None,)
	kioskProfiles: Optional[list[WindowsKioskProfile]] = Field(alias="kioskProfiles", default=None,)
	windowsKioskForceUpdateSchedule: Optional[WindowsKioskForceUpdateSchedule] = Field(alias="windowsKioskForceUpdateSchedule", default=None,)

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
from .windows_kiosk_profile import WindowsKioskProfile
from .windows_kiosk_force_update_schedule import WindowsKioskForceUpdateSchedule

