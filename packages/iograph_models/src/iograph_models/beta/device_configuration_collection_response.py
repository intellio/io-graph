from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidCertificateProfileBase, AndroidForWorkImportedPFXCertificateProfile, AndroidImportedPFXCertificateProfile, AndroidPkcsCertificateProfile, AndroidScepCertificateProfile, AndroidCustomConfiguration, AndroidDeviceOwnerCertificateProfileBase, AndroidDeviceOwnerImportedPFXCertificateProfile, AndroidDeviceOwnerPkcsCertificateProfile, AndroidDeviceOwnerScepCertificateProfile, AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration, AndroidDeviceOwnerGeneralDeviceConfiguration, AndroidDeviceOwnerTrustedRootCertificate, AndroidDeviceOwnerWiFiConfiguration, AndroidDeviceOwnerEnterpriseWiFiConfiguration, AndroidEasEmailProfileConfiguration, AndroidForWorkCertificateProfileBase, AndroidForWorkPkcsCertificateProfile, AndroidForWorkScepCertificateProfile, AndroidForWorkCustomConfiguration, AndroidForWorkEasEmailProfileBase, AndroidForWorkGmailEasConfiguration, AndroidForWorkNineWorkEasConfiguration, AndroidForWorkGeneralDeviceConfiguration, AndroidForWorkTrustedRootCertificate, AndroidForWorkVpnConfiguration, AndroidForWorkWiFiConfiguration, AndroidForWorkEnterpriseWiFiConfiguration, AndroidGeneralDeviceConfiguration, AndroidOmaCpConfiguration, AndroidTrustedRootCertificate, AndroidVpnConfiguration, AndroidWiFiConfiguration, AndroidEnterpriseWiFiConfiguration, AndroidWorkProfileCertificateProfileBase, AndroidWorkProfilePkcsCertificateProfile, AndroidWorkProfileScepCertificateProfile, AndroidWorkProfileCustomConfiguration, AndroidWorkProfileEasEmailProfileBase, AndroidWorkProfileGmailEasConfiguration, AndroidWorkProfileNineWorkEasConfiguration, AndroidWorkProfileGeneralDeviceConfiguration, AndroidWorkProfileTrustedRootCertificate, AndroidWorkProfileVpnConfiguration, AndroidWorkProfileWiFiConfiguration, AndroidWorkProfileEnterpriseWiFiConfiguration, AospDeviceOwnerCertificateProfileBase, AospDeviceOwnerPkcsCertificateProfile, AospDeviceOwnerScepCertificateProfile, AospDeviceOwnerDeviceConfiguration, AospDeviceOwnerTrustedRootCertificate, AospDeviceOwnerWiFiConfiguration, AospDeviceOwnerEnterpriseWiFiConfiguration, AppleDeviceFeaturesConfigurationBase, IosDeviceFeaturesConfiguration, MacOSDeviceFeaturesConfiguration, AppleExpeditedCheckinConfigurationBase, IosExpeditedCheckinConfiguration, AppleVpnConfiguration, IosVpnConfiguration, IosikEv2VpnConfiguration, MacOSVpnConfiguration, EasEmailProfileConfigurationBase, IosEasEmailProfileConfiguration, Windows10EasEmailProfileConfiguration, WindowsPhoneEASEmailProfileConfiguration, EditionUpgradeConfiguration, IosCertificateProfile, IosCertificateProfileBase, IosPkcsCertificateProfile, IosScepCertificateProfile, IosImportedPFXCertificateProfile, IosCustomConfiguration, IosDerivedCredentialAuthenticationConfiguration, IosEducationDeviceConfiguration, IosEduDeviceConfiguration, IosGeneralDeviceConfiguration, IosTrustedRootCertificate, IosUpdateConfiguration, IosWiFiConfiguration, IosEnterpriseWiFiConfiguration, MacOSCertificateProfileBase, MacOSImportedPFXCertificateProfile, MacOSPkcsCertificateProfile, MacOSScepCertificateProfile, MacOSCustomAppConfiguration, MacOSCustomConfiguration, MacOSEndpointProtectionConfiguration, MacOSExtensionsConfiguration, MacOSGeneralDeviceConfiguration, MacOSSoftwareUpdateConfiguration, MacOSTrustedRootCertificate, MacOSWiFiConfiguration, MacOSEnterpriseWiFiConfiguration, MacOSWiredNetworkConfiguration, SharedPCConfiguration, UnsupportedDeviceConfiguration, VpnConfiguration, AndroidDeviceOwnerVpnConfiguration, Windows10CustomConfiguration, Windows10DeviceFirmwareConfigurationInterface, Windows10EndpointProtectionConfiguration, Windows10EnterpriseModernAppManagementConfiguration, Windows10GeneralConfiguration, Windows10NetworkBoundaryConfiguration, Windows10PFXImportCertificateProfile, Windows10SecureAssessmentConfiguration, Windows10TeamGeneralConfiguration, Windows81GeneralConfiguration, Windows81TrustedRootCertificate, Windows81WifiImportConfiguration, WindowsCertificateProfileBase, Windows10CertificateProfileBase, Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81CertificateProfileBase, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile, WindowsDefenderAdvancedThreatProtectionConfiguration, WindowsDeliveryOptimizationConfiguration, WindowsDomainJoinConfiguration, WindowsHealthMonitoringConfiguration, WindowsIdentityProtectionConfiguration, WindowsKioskConfiguration, WindowsPhone81CertificateProfileBase, WindowsPhone81SCEPCertificateProfile, WindowsPhone81CustomConfiguration, WindowsPhone81GeneralConfiguration, WindowsPhone81TrustedRootCertificate, WindowsUpdateForBusinessConfiguration, WindowsVpnConfiguration, Windows10VpnConfiguration, Windows81VpnConfiguration, WindowsPhone81VpnConfiguration, WindowsWifiConfiguration, WindowsWifiEnterpriseEAPConfiguration, WindowsWiredNetworkConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_certificate_profile_base import AndroidCertificateProfileBase
from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
from .android_scep_certificate_profile import AndroidScepCertificateProfile
from .android_custom_configuration import AndroidCustomConfiguration
from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
from .android_oma_cp_configuration import AndroidOmaCpConfiguration
from .android_trusted_root_certificate import AndroidTrustedRootCertificate
from .android_vpn_configuration import AndroidVpnConfiguration
from .android_wi_fi_configuration import AndroidWiFiConfiguration
from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
from .apple_vpn_configuration import AppleVpnConfiguration
from .ios_vpn_configuration import IosVpnConfiguration
from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
from .edition_upgrade_configuration import EditionUpgradeConfiguration
from .ios_certificate_profile import IosCertificateProfile
from .ios_certificate_profile_base import IosCertificateProfileBase
from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
from .ios_scep_certificate_profile import IosScepCertificateProfile
from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
from .ios_custom_configuration import IosCustomConfiguration
from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
from .ios_education_device_configuration import IosEducationDeviceConfiguration
from .ios_edu_device_configuration import IosEduDeviceConfiguration
from .ios_general_device_configuration import IosGeneralDeviceConfiguration
from .ios_trusted_root_certificate import IosTrustedRootCertificate
from .ios_update_configuration import IosUpdateConfiguration
from .ios_wi_fi_configuration import IosWiFiConfiguration
from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
from .mac_o_s_custom_configuration import MacOSCustomConfiguration
from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
from .shared_p_c_configuration import SharedPCConfiguration
from .unsupported_device_configuration import UnsupportedDeviceConfiguration
from .vpn_configuration import VpnConfiguration
from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
from .windows10_custom_configuration import Windows10CustomConfiguration
from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
from .windows10_general_configuration import Windows10GeneralConfiguration
from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
from .windows81_general_configuration import Windows81GeneralConfiguration
from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
from .windows_certificate_profile_base import WindowsCertificateProfileBase
from .windows10_certificate_profile_base import Windows10CertificateProfileBase
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_certificate_profile_base import Windows81CertificateProfileBase
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
from .windows_kiosk_configuration import WindowsKioskConfiguration
from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
from .windows_vpn_configuration import WindowsVpnConfiguration
from .windows10_vpn_configuration import Windows10VpnConfiguration
from .windows81_vpn_configuration import Windows81VpnConfiguration
from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
from .windows_wifi_configuration import WindowsWifiConfiguration
from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration

