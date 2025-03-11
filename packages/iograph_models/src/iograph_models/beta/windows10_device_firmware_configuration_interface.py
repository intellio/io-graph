from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10DeviceFirmwareConfigurationInterface(BaseModel):
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
	bluetooth: Optional[Enablement | str] = Field(alias="bluetooth",default=None,)
	bootFromBuiltInNetworkAdapters: Optional[Enablement | str] = Field(alias="bootFromBuiltInNetworkAdapters",default=None,)
	bootFromExternalMedia: Optional[Enablement | str] = Field(alias="bootFromExternalMedia",default=None,)
	cameras: Optional[Enablement | str] = Field(alias="cameras",default=None,)
	changeUefiSettingsPermission: Optional[ChangeUefiSettingsPermission | str] = Field(alias="changeUefiSettingsPermission",default=None,)
	frontCamera: Optional[Enablement | str] = Field(alias="frontCamera",default=None,)
	infraredCamera: Optional[Enablement | str] = Field(alias="infraredCamera",default=None,)
	microphone: Optional[Enablement | str] = Field(alias="microphone",default=None,)
	microphonesAndSpeakers: Optional[Enablement | str] = Field(alias="microphonesAndSpeakers",default=None,)
	nearFieldCommunication: Optional[Enablement | str] = Field(alias="nearFieldCommunication",default=None,)
	radios: Optional[Enablement | str] = Field(alias="radios",default=None,)
	rearCamera: Optional[Enablement | str] = Field(alias="rearCamera",default=None,)
	sdCard: Optional[Enablement | str] = Field(alias="sdCard",default=None,)
	simultaneousMultiThreading: Optional[Enablement | str] = Field(alias="simultaneousMultiThreading",default=None,)
	usbTypeAPort: Optional[Enablement | str] = Field(alias="usbTypeAPort",default=None,)
	virtualizationOfCpuAndIO: Optional[Enablement | str] = Field(alias="virtualizationOfCpuAndIO",default=None,)
	wakeOnLAN: Optional[Enablement | str] = Field(alias="wakeOnLAN",default=None,)
	wakeOnPower: Optional[Enablement | str] = Field(alias="wakeOnPower",default=None,)
	wiFi: Optional[Enablement | str] = Field(alias="wiFi",default=None,)
	windowsPlatformBinaryTable: Optional[Enablement | str] = Field(alias="windowsPlatformBinaryTable",default=None,)
	wirelessWideAreaNetwork: Optional[Enablement | str] = Field(alias="wirelessWideAreaNetwork",default=None,)

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
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .change_uefi_settings_permission import ChangeUefiSettingsPermission
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement

