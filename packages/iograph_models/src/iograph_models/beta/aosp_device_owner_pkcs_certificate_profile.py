from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AospDeviceOwnerPkcsCertificateProfile(BaseModel):
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
	certificateValidityPeriodScale: Optional[CertificateValidityPeriodScale | str] = Field(alias="certificateValidityPeriodScale",default=None,)
	certificateValidityPeriodValue: Optional[int] = Field(alias="certificateValidityPeriodValue",default=None,)
	extendedKeyUsages: Optional[list[ExtendedKeyUsage]] = Field(alias="extendedKeyUsages",default=None,)
	renewalThresholdPercentage: Optional[int] = Field(alias="renewalThresholdPercentage",default=None,)
	subjectAlternativeNameType: Optional[SubjectAlternativeNameType | str] = Field(alias="subjectAlternativeNameType",default=None,)
	subjectNameFormat: Optional[SubjectNameFormat | str] = Field(alias="subjectNameFormat",default=None,)
	rootCertificate: Optional[AospDeviceOwnerTrustedRootCertificate] = Field(alias="rootCertificate",default=None,)
	certificateStore: Optional[CertificateStore | str] = Field(alias="certificateStore",default=None,)
	certificateTemplateName: Optional[str] = Field(alias="certificateTemplateName",default=None,)
	certificationAuthority: Optional[str] = Field(alias="certificationAuthority",default=None,)
	certificationAuthorityName: Optional[str] = Field(alias="certificationAuthorityName",default=None,)
	certificationAuthorityType: Optional[DeviceManagementCertificationAuthority | str] = Field(alias="certificationAuthorityType",default=None,)
	customSubjectAlternativeNames: Optional[list[CustomSubjectAlternativeName]] = Field(alias="customSubjectAlternativeNames",default=None,)
	subjectAlternativeNameFormatString: Optional[str] = Field(alias="subjectAlternativeNameFormatString",default=None,)
	subjectNameFormatString: Optional[str] = Field(alias="subjectNameFormatString",default=None,)
	managedDeviceCertificateStates: Optional[list[ManagedDeviceCertificateState]] = Field(alias="managedDeviceCertificateStates",default=None,)

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
from .extended_key_usage import ExtendedKeyUsage
from .subject_alternative_name_type import SubjectAlternativeNameType
from .subject_name_format import SubjectNameFormat
from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
from .certificate_store import CertificateStore
from .device_management_certification_authority import DeviceManagementCertificationAuthority
from .custom_subject_alternative_name import CustomSubjectAlternativeName
from .managed_device_certificate_state import ManagedDeviceCertificateState

