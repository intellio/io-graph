from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSEndpointProtectionConfiguration(BaseModel):
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
	advancedThreatProtectionAutomaticSampleSubmission: Optional[Enablement | str] = Field(alias="advancedThreatProtectionAutomaticSampleSubmission",default=None,)
	advancedThreatProtectionCloudDelivered: Optional[Enablement | str] = Field(alias="advancedThreatProtectionCloudDelivered",default=None,)
	advancedThreatProtectionDiagnosticDataCollection: Optional[Enablement | str] = Field(alias="advancedThreatProtectionDiagnosticDataCollection",default=None,)
	advancedThreatProtectionExcludedExtensions: Optional[list[str]] = Field(alias="advancedThreatProtectionExcludedExtensions",default=None,)
	advancedThreatProtectionExcludedFiles: Optional[list[str]] = Field(alias="advancedThreatProtectionExcludedFiles",default=None,)
	advancedThreatProtectionExcludedFolders: Optional[list[str]] = Field(alias="advancedThreatProtectionExcludedFolders",default=None,)
	advancedThreatProtectionExcludedProcesses: Optional[list[str]] = Field(alias="advancedThreatProtectionExcludedProcesses",default=None,)
	advancedThreatProtectionRealTime: Optional[Enablement | str] = Field(alias="advancedThreatProtectionRealTime",default=None,)
	fileVaultAllowDeferralUntilSignOut: Optional[bool] = Field(alias="fileVaultAllowDeferralUntilSignOut",default=None,)
	fileVaultDisablePromptAtSignOut: Optional[bool] = Field(alias="fileVaultDisablePromptAtSignOut",default=None,)
	fileVaultEnabled: Optional[bool] = Field(alias="fileVaultEnabled",default=None,)
	fileVaultHidePersonalRecoveryKey: Optional[bool] = Field(alias="fileVaultHidePersonalRecoveryKey",default=None,)
	fileVaultInstitutionalRecoveryKeyCertificate: Optional[str] = Field(alias="fileVaultInstitutionalRecoveryKeyCertificate",default=None,)
	fileVaultInstitutionalRecoveryKeyCertificateFileName: Optional[str] = Field(alias="fileVaultInstitutionalRecoveryKeyCertificateFileName",default=None,)
	fileVaultNumberOfTimesUserCanIgnore: Optional[int] = Field(alias="fileVaultNumberOfTimesUserCanIgnore",default=None,)
	fileVaultPersonalRecoveryKeyHelpMessage: Optional[str] = Field(alias="fileVaultPersonalRecoveryKeyHelpMessage",default=None,)
	fileVaultPersonalRecoveryKeyRotationInMonths: Optional[int] = Field(alias="fileVaultPersonalRecoveryKeyRotationInMonths",default=None,)
	fileVaultSelectedRecoveryKeyTypes: Optional[MacOSFileVaultRecoveryKeyTypes | str] = Field(alias="fileVaultSelectedRecoveryKeyTypes",default=None,)
	firewallApplications: Optional[list[MacOSFirewallApplication]] = Field(alias="firewallApplications",default=None,)
	firewallBlockAllIncoming: Optional[bool] = Field(alias="firewallBlockAllIncoming",default=None,)
	firewallEnabled: Optional[bool] = Field(alias="firewallEnabled",default=None,)
	firewallEnableStealthMode: Optional[bool] = Field(alias="firewallEnableStealthMode",default=None,)
	gatekeeperAllowedAppSource: Optional[MacOSGatekeeperAppSources | str] = Field(alias="gatekeeperAllowedAppSource",default=None,)
	gatekeeperBlockOverride: Optional[bool] = Field(alias="gatekeeperBlockOverride",default=None,)

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
from .mac_o_s_file_vault_recovery_key_types import MacOSFileVaultRecoveryKeyTypes
from .mac_o_s_firewall_application import MacOSFirewallApplication
from .mac_o_s_gatekeeper_app_sources import MacOSGatekeeperAppSources

