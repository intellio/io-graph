from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDeliveryOptimizationConfiguration(BaseModel):
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
	backgroundDownloadFromHttpDelayInSeconds: Optional[int] = Field(alias="backgroundDownloadFromHttpDelayInSeconds",default=None,)
	bandwidthMode: SerializeAsAny[Optional[DeliveryOptimizationBandwidth]] = Field(alias="bandwidthMode",default=None,)
	cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds: Optional[int] = Field(alias="cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds",default=None,)
	cacheServerForegroundDownloadFallbackToHttpDelayInSeconds: Optional[int] = Field(alias="cacheServerForegroundDownloadFallbackToHttpDelayInSeconds",default=None,)
	cacheServerHostNames: Optional[list[str]] = Field(alias="cacheServerHostNames",default=None,)
	deliveryOptimizationMode: Optional[WindowsDeliveryOptimizationMode | str] = Field(alias="deliveryOptimizationMode",default=None,)
	foregroundDownloadFromHttpDelayInSeconds: Optional[int] = Field(alias="foregroundDownloadFromHttpDelayInSeconds",default=None,)
	groupIdSource: SerializeAsAny[Optional[DeliveryOptimizationGroupIdSource]] = Field(alias="groupIdSource",default=None,)
	maximumCacheAgeInDays: Optional[int] = Field(alias="maximumCacheAgeInDays",default=None,)
	maximumCacheSize: SerializeAsAny[Optional[DeliveryOptimizationMaxCacheSize]] = Field(alias="maximumCacheSize",default=None,)
	minimumBatteryPercentageAllowedToUpload: Optional[int] = Field(alias="minimumBatteryPercentageAllowedToUpload",default=None,)
	minimumDiskSizeAllowedToPeerInGigabytes: Optional[int] = Field(alias="minimumDiskSizeAllowedToPeerInGigabytes",default=None,)
	minimumFileSizeToCacheInMegabytes: Optional[int] = Field(alias="minimumFileSizeToCacheInMegabytes",default=None,)
	minimumRamAllowedToPeerInGigabytes: Optional[int] = Field(alias="minimumRamAllowedToPeerInGigabytes",default=None,)
	modifyCacheLocation: Optional[str] = Field(alias="modifyCacheLocation",default=None,)
	restrictPeerSelectionBy: Optional[DeliveryOptimizationRestrictPeerSelectionByOptions | str] = Field(alias="restrictPeerSelectionBy",default=None,)
	vpnPeerCaching: Optional[Enablement | str] = Field(alias="vpnPeerCaching",default=None,)

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
from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode
from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource
from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize
from .delivery_optimization_restrict_peer_selection_by_options import DeliveryOptimizationRestrictPeerSelectionByOptions
from .enablement import Enablement

