from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosDeviceFeaturesConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosDeviceFeaturesConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.iosDeviceFeaturesConfiguration")
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
	airPrintDestinations: Optional[list[AirPrintDestination]] = Field(alias="airPrintDestinations", default=None,)
	assetTagTemplate: Optional[str] = Field(alias="assetTagTemplate", default=None,)
	contentFilterSettings: Optional[Union[IosWebContentFilterAutoFilter, IosWebContentFilterSpecificWebsitesAccess]] = Field(alias="contentFilterSettings", default=None,discriminator="odata_type", )
	homeScreenDockIcons: Optional[list[Annotated[Union[IosHomeScreenApp, IosHomeScreenFolder],Field(discriminator="odata_type")]]] = Field(alias="homeScreenDockIcons", default=None,)
	homeScreenGridHeight: Optional[int] = Field(alias="homeScreenGridHeight", default=None,)
	homeScreenGridWidth: Optional[int] = Field(alias="homeScreenGridWidth", default=None,)
	homeScreenPages: Optional[list[IosHomeScreenPage]] = Field(alias="homeScreenPages", default=None,)
	iosSingleSignOnExtension: Optional[Union[IosAzureAdSingleSignOnExtension, IosCredentialSingleSignOnExtension, IosKerberosSingleSignOnExtension, IosRedirectSingleSignOnExtension]] = Field(alias="iosSingleSignOnExtension", default=None,discriminator="odata_type", )
	lockScreenFootnote: Optional[str] = Field(alias="lockScreenFootnote", default=None,)
	notificationSettings: Optional[list[IosNotificationSettings]] = Field(alias="notificationSettings", default=None,)
	singleSignOnExtension: Optional[Union[CredentialSingleSignOnExtension, IosSingleSignOnExtension, IosAzureAdSingleSignOnExtension, IosCredentialSingleSignOnExtension, IosKerberosSingleSignOnExtension, IosRedirectSingleSignOnExtension, KerberosSingleSignOnExtension, MacOSSingleSignOnExtension, MacOSAzureAdSingleSignOnExtension, MacOSCredentialSingleSignOnExtension, MacOSKerberosSingleSignOnExtension, MacOSRedirectSingleSignOnExtension, RedirectSingleSignOnExtension]] = Field(alias="singleSignOnExtension", default=None,discriminator="odata_type", )
	singleSignOnSettings: Optional[IosSingleSignOnSettings] = Field(alias="singleSignOnSettings", default=None,)
	wallpaperDisplayLocation: Optional[IosWallpaperDisplayLocation | str] = Field(alias="wallpaperDisplayLocation", default=None,)
	wallpaperImage: Optional[MimeContent] = Field(alias="wallpaperImage", default=None,)
	identityCertificateForClientAuthentication: Optional[Union[IosPkcsCertificateProfile, IosScepCertificateProfile]] = Field(alias="identityCertificateForClientAuthentication", default=None,discriminator="odata_type", )
	singleSignOnExtensionPkinitCertificate: Optional[Union[IosPkcsCertificateProfile, IosScepCertificateProfile]] = Field(alias="singleSignOnExtensionPkinitCertificate", default=None,discriminator="odata_type", )

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
from .air_print_destination import AirPrintDestination
from .ios_web_content_filter_auto_filter import IosWebContentFilterAutoFilter
from .ios_web_content_filter_specific_websites_access import IosWebContentFilterSpecificWebsitesAccess
from .ios_home_screen_app import IosHomeScreenApp
from .ios_home_screen_folder import IosHomeScreenFolder
from .ios_home_screen_page import IosHomeScreenPage
from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
from .ios_notification_settings import IosNotificationSettings
from .credential_single_sign_on_extension import CredentialSingleSignOnExtension
from .ios_single_sign_on_extension import IosSingleSignOnExtension
from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
from .kerberos_single_sign_on_extension import KerberosSingleSignOnExtension
from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
from .redirect_single_sign_on_extension import RedirectSingleSignOnExtension
from .ios_single_sign_on_settings import IosSingleSignOnSettings
from .ios_wallpaper_display_location import IosWallpaperDisplayLocation
from .mime_content import MimeContent
from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
from .ios_scep_certificate_profile import IosScepCertificateProfile
from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
from .ios_scep_certificate_profile import IosScepCertificateProfile

