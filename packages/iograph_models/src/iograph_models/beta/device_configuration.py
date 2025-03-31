from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile":
				from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
				return AndroidForWorkImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidImportedPFXCertificateProfile":
				from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
				return AndroidImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidPkcsCertificateProfile":
				from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
				return AndroidPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidScepCertificateProfile":
				from .android_scep_certificate_profile import AndroidScepCertificateProfile
				return AndroidScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidCustomConfiguration":
				from .android_custom_configuration import AndroidCustomConfiguration
				return AndroidCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile":
				from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
				return AndroidDeviceOwnerImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile":
				from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
				return AndroidDeviceOwnerPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerScepCertificateProfile":
				from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
				return AndroidDeviceOwnerScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration":
				from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
				return AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration":
				from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
				return AndroidDeviceOwnerGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerTrustedRootCertificate":
				from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
				return AndroidDeviceOwnerTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration":
				from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
				return AndroidDeviceOwnerEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidEasEmailProfileConfiguration":
				from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
				return AndroidEasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkPkcsCertificateProfile":
				from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
				return AndroidForWorkPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkScepCertificateProfile":
				from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
				return AndroidForWorkScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkCustomConfiguration":
				from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
				return AndroidForWorkCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkGmailEasConfiguration":
				from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
				return AndroidForWorkGmailEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkNineWorkEasConfiguration":
				from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
				return AndroidForWorkNineWorkEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkGeneralDeviceConfiguration":
				from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
				return AndroidForWorkGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkTrustedRootCertificate":
				from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
				return AndroidForWorkTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkVpnConfiguration":
				from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
				return AndroidForWorkVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration":
				from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
				return AndroidForWorkEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidGeneralDeviceConfiguration":
				from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
				return AndroidGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidOmaCpConfiguration":
				from .android_oma_cp_configuration import AndroidOmaCpConfiguration
				return AndroidOmaCpConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidTrustedRootCertificate":
				from .android_trusted_root_certificate import AndroidTrustedRootCertificate
				return AndroidTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidVpnConfiguration":
				from .android_vpn_configuration import AndroidVpnConfiguration
				return AndroidVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidEnterpriseWiFiConfiguration":
				from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
				return AndroidEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfilePkcsCertificateProfile":
				from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
				return AndroidWorkProfilePkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileScepCertificateProfile":
				from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
				return AndroidWorkProfileScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCustomConfiguration":
				from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
				return AndroidWorkProfileCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileGmailEasConfiguration":
				from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
				return AndroidWorkProfileGmailEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration":
				from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
				return AndroidWorkProfileNineWorkEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
				from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
				return AndroidWorkProfileGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileTrustedRootCertificate":
				from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
				return AndroidWorkProfileTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileVpnConfiguration":
				from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
				return AndroidWorkProfileVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration":
				from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
				return AndroidWorkProfileEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile":
				from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
				return AospDeviceOwnerPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerScepCertificateProfile":
				from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
				return AospDeviceOwnerScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerDeviceConfiguration":
				from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
				return AospDeviceOwnerDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerTrustedRootCertificate":
				from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
				return AospDeviceOwnerTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration":
				from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
				return AospDeviceOwnerEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosDeviceFeaturesConfiguration":
				from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
				return IosDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
				from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
				return MacOSDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosExpeditedCheckinConfiguration":
				from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
				return IosExpeditedCheckinConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosikEv2VpnConfiguration":
				from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
				return IosikEv2VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSVpnConfiguration":
				from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
				return MacOSVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEasEmailProfileConfiguration":
				from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
				return IosEasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EasEmailProfileConfiguration":
				from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
				return Windows10EasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration":
				from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
				return WindowsPhoneEASEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.editionUpgradeConfiguration":
				from .edition_upgrade_configuration import EditionUpgradeConfiguration
				return EditionUpgradeConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosPkcsCertificateProfile":
				from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
				return IosPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosScepCertificateProfile":
				from .ios_scep_certificate_profile import IosScepCertificateProfile
				return IosScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosImportedPFXCertificateProfile":
				from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
				return IosImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCustomConfiguration":
				from .ios_custom_configuration import IosCustomConfiguration
				return IosCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration":
				from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
				return IosDerivedCredentialAuthenticationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEducationDeviceConfiguration":
				from .ios_education_device_configuration import IosEducationDeviceConfiguration
				return IosEducationDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEduDeviceConfiguration":
				from .ios_edu_device_configuration import IosEduDeviceConfiguration
				return IosEduDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosGeneralDeviceConfiguration":
				from .ios_general_device_configuration import IosGeneralDeviceConfiguration
				return IosGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosTrustedRootCertificate":
				from .ios_trusted_root_certificate import IosTrustedRootCertificate
				return IosTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.iosUpdateConfiguration":
				from .ios_update_configuration import IosUpdateConfiguration
				return IosUpdateConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEnterpriseWiFiConfiguration":
				from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
				return IosEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSImportedPFXCertificateProfile":
				from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
				return MacOSImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSPkcsCertificateProfile":
				from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
				return MacOSPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSScepCertificateProfile":
				from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
				return MacOSScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCustomAppConfiguration":
				from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
				return MacOSCustomAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCustomConfiguration":
				from .mac_o_s_custom_configuration import MacOSCustomConfiguration
				return MacOSCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSEndpointProtectionConfiguration":
				from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
				return MacOSEndpointProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSExtensionsConfiguration":
				from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
				return MacOSExtensionsConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSGeneralDeviceConfiguration":
				from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
				return MacOSGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSSoftwareUpdateConfiguration":
				from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
				return MacOSSoftwareUpdateConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSTrustedRootCertificate":
				from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
				return MacOSTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSEnterpriseWiFiConfiguration":
				from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
				return MacOSEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSWiredNetworkConfiguration":
				from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
				return MacOSWiredNetworkConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedPCConfiguration":
				from .shared_p_c_configuration import SharedPCConfiguration
				return SharedPCConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.unsupportedDeviceConfiguration":
				from .unsupported_device_configuration import UnsupportedDeviceConfiguration
				return UnsupportedDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerVpnConfiguration":
				from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
				return AndroidDeviceOwnerVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CustomConfiguration":
				from .windows10_custom_configuration import Windows10CustomConfiguration
				return Windows10CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface":
				from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
				return Windows10DeviceFirmwareConfigurationInterface.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EndpointProtectionConfiguration":
				from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
				return Windows10EndpointProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
				from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
				return Windows10EnterpriseModernAppManagementConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10GeneralConfiguration":
				from .windows10_general_configuration import Windows10GeneralConfiguration
				return Windows10GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10NetworkBoundaryConfiguration":
				from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
				return Windows10NetworkBoundaryConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10PFXImportCertificateProfile":
				from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
				return Windows10PFXImportCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10SecureAssessmentConfiguration":
				from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
				return Windows10SecureAssessmentConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10TeamGeneralConfiguration":
				from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
				return Windows10TeamGeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81GeneralConfiguration":
				from .windows81_general_configuration import Windows81GeneralConfiguration
				return Windows81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81TrustedRootCertificate":
				from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
				return Windows81TrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81WifiImportConfiguration":
				from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
				return Windows81WifiImportConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10PkcsCertificateProfile":
				from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
				return Windows10PkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10ImportedPFXCertificateProfile":
				from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
				return Windows10ImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81SCEPCertificateProfile":
				from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
				return Windows81SCEPCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile":
				from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
				return WindowsPhone81ImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
				from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
				return WindowsDefenderAdvancedThreatProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDeliveryOptimizationConfiguration":
				from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
				return WindowsDeliveryOptimizationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDomainJoinConfiguration":
				from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
				return WindowsDomainJoinConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsHealthMonitoringConfiguration":
				from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
				return WindowsHealthMonitoringConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsIdentityProtectionConfiguration":
				from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
				return WindowsIdentityProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskConfiguration":
				from .windows_kiosk_configuration import WindowsKioskConfiguration
				return WindowsKioskConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81SCEPCertificateProfile":
				from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
				return WindowsPhone81SCEPCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CustomConfiguration":
				from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
				return WindowsPhone81CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81GeneralConfiguration":
				from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
				return WindowsPhone81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81TrustedRootCertificate":
				from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
				return WindowsPhone81TrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
				from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
				return WindowsUpdateForBusinessConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10VpnConfiguration":
				from .windows10_vpn_configuration import Windows10VpnConfiguration
				return Windows10VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81VpnConfiguration":
				from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
				return WindowsPhone81VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration":
				from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
				return WindowsWifiEnterpriseEAPConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWiredNetworkConfiguration":
				from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
				return WindowsWiredNetworkConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

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
