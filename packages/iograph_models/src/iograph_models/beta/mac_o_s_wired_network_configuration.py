from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSWiredNetworkConfiguration(BaseModel):
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
	authenticationMethod: Optional[WiFiAuthenticationMethod | str] = Field(alias="authenticationMethod",default=None,)
	deploymentChannel: Optional[AppleDeploymentChannel | str] = Field(alias="deploymentChannel",default=None,)
	eapFastConfiguration: Optional[EapFastConfiguration | str] = Field(alias="eapFastConfiguration",default=None,)
	eapType: Optional[EapType | str] = Field(alias="eapType",default=None,)
	enableOuterIdentityPrivacy: Optional[str] = Field(alias="enableOuterIdentityPrivacy",default=None,)
	networkInterface: Optional[WiredNetworkInterface | str] = Field(alias="networkInterface",default=None,)
	networkName: Optional[str] = Field(alias="networkName",default=None,)
	nonEapAuthenticationMethodForEapTtls: Optional[NonEapAuthenticationMethodForEapTtlsType | str] = Field(alias="nonEapAuthenticationMethodForEapTtls",default=None,)
	trustedServerCertificateNames: Optional[list[str]] = Field(alias="trustedServerCertificateNames",default=None,)
	identityCertificateForClientAuthentication: SerializeAsAny[Optional[MacOSCertificateProfileBase]] = Field(alias="identityCertificateForClientAuthentication",default=None,)
	rootCertificateForServerValidation: Optional[MacOSTrustedRootCertificate] = Field(alias="rootCertificateForServerValidation",default=None,)

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
from .wi_fi_authentication_method import WiFiAuthenticationMethod
from .apple_deployment_channel import AppleDeploymentChannel
from .eap_fast_configuration import EapFastConfiguration
from .eap_type import EapType
from .wired_network_interface import WiredNetworkInterface
from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate

