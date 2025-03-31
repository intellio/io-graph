from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSScepCertificateProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSScepCertificateProfile"] = Field(alias="@odata.type", default="#microsoft.graph.macOSScepCertificateProfile")
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
	certificateValidityPeriodScale: Optional[CertificateValidityPeriodScale | str] = Field(alias="certificateValidityPeriodScale", default=None,)
	certificateValidityPeriodValue: Optional[int] = Field(alias="certificateValidityPeriodValue", default=None,)
	renewalThresholdPercentage: Optional[int] = Field(alias="renewalThresholdPercentage", default=None,)
	subjectAlternativeNameType: Optional[SubjectAlternativeNameType | str] = Field(alias="subjectAlternativeNameType", default=None,)
	subjectNameFormat: Optional[AppleSubjectNameFormat | str] = Field(alias="subjectNameFormat", default=None,)
	allowAllAppsAccess: Optional[bool] = Field(alias="allowAllAppsAccess", default=None,)
	certificateStore: Optional[CertificateStore | str] = Field(alias="certificateStore", default=None,)
	customSubjectAlternativeNames: Optional[list[CustomSubjectAlternativeName]] = Field(alias="customSubjectAlternativeNames", default=None,)
	deploymentChannel: Optional[AppleDeploymentChannel | str] = Field(alias="deploymentChannel", default=None,)
	extendedKeyUsages: Optional[list[ExtendedKeyUsage]] = Field(alias="extendedKeyUsages", default=None,)
	hashAlgorithm: Optional[HashAlgorithms | str] = Field(alias="hashAlgorithm", default=None,)
	keySize: Optional[KeySize | str] = Field(alias="keySize", default=None,)
	keyUsage: Optional[KeyUsages | str] = Field(alias="keyUsage", default=None,)
	scepServerUrls: Optional[list[str]] = Field(alias="scepServerUrls", default=None,)
	subjectAlternativeNameFormatString: Optional[str] = Field(alias="subjectAlternativeNameFormatString", default=None,)
	subjectNameFormatString: Optional[str] = Field(alias="subjectNameFormatString", default=None,)
	managedDeviceCertificateStates: Optional[list[ManagedDeviceCertificateState]] = Field(alias="managedDeviceCertificateStates", default=None,)
	rootCertificate: Optional[MacOSTrustedRootCertificate] = Field(alias="rootCertificate", default=None,)

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
from .certificate_validity_period_scale import CertificateValidityPeriodScale
from .subject_alternative_name_type import SubjectAlternativeNameType
from .apple_subject_name_format import AppleSubjectNameFormat
from .certificate_store import CertificateStore
from .custom_subject_alternative_name import CustomSubjectAlternativeName
from .apple_deployment_channel import AppleDeploymentChannel
from .extended_key_usage import ExtendedKeyUsage
from .hash_algorithms import HashAlgorithms
from .key_size import KeySize
from .key_usages import KeyUsages
from .managed_device_certificate_state import ManagedDeviceCertificateState
from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
