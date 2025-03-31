from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsIdentityProtectionConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsIdentityProtectionConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsIdentityProtectionConfiguration")
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
	enhancedAntiSpoofingForFacialFeaturesEnabled: Optional[bool] = Field(alias="enhancedAntiSpoofingForFacialFeaturesEnabled", default=None,)
	pinExpirationInDays: Optional[int] = Field(alias="pinExpirationInDays", default=None,)
	pinLowercaseCharactersUsage: Optional[ConfigurationUsage | str] = Field(alias="pinLowercaseCharactersUsage", default=None,)
	pinMaximumLength: Optional[int] = Field(alias="pinMaximumLength", default=None,)
	pinMinimumLength: Optional[int] = Field(alias="pinMinimumLength", default=None,)
	pinPreviousBlockCount: Optional[int] = Field(alias="pinPreviousBlockCount", default=None,)
	pinRecoveryEnabled: Optional[bool] = Field(alias="pinRecoveryEnabled", default=None,)
	pinSpecialCharactersUsage: Optional[ConfigurationUsage | str] = Field(alias="pinSpecialCharactersUsage", default=None,)
	pinUppercaseCharactersUsage: Optional[ConfigurationUsage | str] = Field(alias="pinUppercaseCharactersUsage", default=None,)
	securityDeviceRequired: Optional[bool] = Field(alias="securityDeviceRequired", default=None,)
	unlockWithBiometricsEnabled: Optional[bool] = Field(alias="unlockWithBiometricsEnabled", default=None,)
	useCertificatesForOnPremisesAuthEnabled: Optional[bool] = Field(alias="useCertificatesForOnPremisesAuthEnabled", default=None,)
	useSecurityKeyForSignin: Optional[bool] = Field(alias="useSecurityKeyForSignin", default=None,)
	windowsHelloForBusinessBlocked: Optional[bool] = Field(alias="windowsHelloForBusinessBlocked", default=None,)

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
from .configuration_usage import ConfigurationUsage
