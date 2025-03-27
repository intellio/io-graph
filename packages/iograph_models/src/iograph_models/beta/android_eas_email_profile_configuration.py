from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidEasEmailProfileConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidEasEmailProfileConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.androidEasEmailProfileConfiguration")
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
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	authenticationMethod: Optional[EasAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	customDomainName: Optional[str] = Field(alias="customDomainName", default=None,)
	durationOfEmailToSync: Optional[EmailSyncDuration | str] = Field(alias="durationOfEmailToSync", default=None,)
	emailAddressSource: Optional[UserEmailSource | str] = Field(alias="emailAddressSource", default=None,)
	emailSyncSchedule: Optional[EmailSyncSchedule | str] = Field(alias="emailSyncSchedule", default=None,)
	hostName: Optional[str] = Field(alias="hostName", default=None,)
	requireSmime: Optional[bool] = Field(alias="requireSmime", default=None,)
	requireSsl: Optional[bool] = Field(alias="requireSsl", default=None,)
	syncCalendar: Optional[bool] = Field(alias="syncCalendar", default=None,)
	syncContacts: Optional[bool] = Field(alias="syncContacts", default=None,)
	syncNotes: Optional[bool] = Field(alias="syncNotes", default=None,)
	syncTasks: Optional[bool] = Field(alias="syncTasks", default=None,)
	userDomainNameSource: Optional[DomainNameSource | str] = Field(alias="userDomainNameSource", default=None,)
	usernameSource: Optional[AndroidUsernameSource | str] = Field(alias="usernameSource", default=None,)
	identityCertificate: Optional[Union[AndroidForWorkImportedPFXCertificateProfile, AndroidImportedPFXCertificateProfile, AndroidPkcsCertificateProfile, AndroidScepCertificateProfile]] = Field(alias="identityCertificate", default=None,discriminator="odata_type", )
	smimeSigningCertificate: Optional[Union[AndroidForWorkImportedPFXCertificateProfile, AndroidImportedPFXCertificateProfile, AndroidPkcsCertificateProfile, AndroidScepCertificateProfile]] = Field(alias="smimeSigningCertificate", default=None,discriminator="odata_type", )

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
from .eas_authentication_method import EasAuthenticationMethod
from .email_sync_duration import EmailSyncDuration
from .user_email_source import UserEmailSource
from .email_sync_schedule import EmailSyncSchedule
from .domain_name_source import DomainNameSource
from .android_username_source import AndroidUsernameSource
from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
from .android_scep_certificate_profile import AndroidScepCertificateProfile
from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
from .android_scep_certificate_profile import AndroidScepCertificateProfile

