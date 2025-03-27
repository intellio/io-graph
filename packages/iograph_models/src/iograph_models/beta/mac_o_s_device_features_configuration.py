from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSDeviceFeaturesConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSDeviceFeaturesConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.macOSDeviceFeaturesConfiguration")
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
	adminShowHostInfo: Optional[bool] = Field(alias="adminShowHostInfo", default=None,)
	appAssociatedDomains: Optional[list[MacOSAssociatedDomainsItem]] = Field(alias="appAssociatedDomains", default=None,)
	associatedDomains: Optional[list[KeyValuePair]] = Field(alias="associatedDomains", default=None,)
	authorizedUsersListHidden: Optional[bool] = Field(alias="authorizedUsersListHidden", default=None,)
	authorizedUsersListHideAdminUsers: Optional[bool] = Field(alias="authorizedUsersListHideAdminUsers", default=None,)
	authorizedUsersListHideLocalUsers: Optional[bool] = Field(alias="authorizedUsersListHideLocalUsers", default=None,)
	authorizedUsersListHideMobileAccounts: Optional[bool] = Field(alias="authorizedUsersListHideMobileAccounts", default=None,)
	authorizedUsersListIncludeNetworkUsers: Optional[bool] = Field(alias="authorizedUsersListIncludeNetworkUsers", default=None,)
	authorizedUsersListShowOtherManagedUsers: Optional[bool] = Field(alias="authorizedUsersListShowOtherManagedUsers", default=None,)
	autoLaunchItems: Optional[list[MacOSLaunchItem]] = Field(alias="autoLaunchItems", default=None,)
	consoleAccessDisabled: Optional[bool] = Field(alias="consoleAccessDisabled", default=None,)
	contentCachingBlockDeletion: Optional[bool] = Field(alias="contentCachingBlockDeletion", default=None,)
	contentCachingClientListenRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range],Field(discriminator="odata_type")]]] = Field(alias="contentCachingClientListenRanges", default=None,)
	contentCachingClientPolicy: Optional[MacOSContentCachingClientPolicy | str] = Field(alias="contentCachingClientPolicy", default=None,)
	contentCachingDataPath: Optional[str] = Field(alias="contentCachingDataPath", default=None,)
	contentCachingDisableConnectionSharing: Optional[bool] = Field(alias="contentCachingDisableConnectionSharing", default=None,)
	contentCachingEnabled: Optional[bool] = Field(alias="contentCachingEnabled", default=None,)
	contentCachingForceConnectionSharing: Optional[bool] = Field(alias="contentCachingForceConnectionSharing", default=None,)
	contentCachingKeepAwake: Optional[bool] = Field(alias="contentCachingKeepAwake", default=None,)
	contentCachingLogClientIdentities: Optional[bool] = Field(alias="contentCachingLogClientIdentities", default=None,)
	contentCachingMaxSizeBytes: Optional[int] = Field(alias="contentCachingMaxSizeBytes", default=None,)
	contentCachingParents: Optional[list[str]] = Field(alias="contentCachingParents", default=None,)
	contentCachingParentSelectionPolicy: Optional[MacOSContentCachingParentSelectionPolicy | str] = Field(alias="contentCachingParentSelectionPolicy", default=None,)
	contentCachingPeerFilterRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range],Field(discriminator="odata_type")]]] = Field(alias="contentCachingPeerFilterRanges", default=None,)
	contentCachingPeerListenRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range],Field(discriminator="odata_type")]]] = Field(alias="contentCachingPeerListenRanges", default=None,)
	contentCachingPeerPolicy: Optional[MacOSContentCachingPeerPolicy | str] = Field(alias="contentCachingPeerPolicy", default=None,)
	contentCachingPort: Optional[int] = Field(alias="contentCachingPort", default=None,)
	contentCachingPublicRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range],Field(discriminator="odata_type")]]] = Field(alias="contentCachingPublicRanges", default=None,)
	contentCachingShowAlerts: Optional[bool] = Field(alias="contentCachingShowAlerts", default=None,)
	contentCachingType: Optional[MacOSContentCachingType | str] = Field(alias="contentCachingType", default=None,)
	loginWindowText: Optional[str] = Field(alias="loginWindowText", default=None,)
	logOutDisabledWhileLoggedIn: Optional[bool] = Field(alias="logOutDisabledWhileLoggedIn", default=None,)
	macOSSingleSignOnExtension: Optional[Union[MacOSAzureAdSingleSignOnExtension, MacOSCredentialSingleSignOnExtension, MacOSKerberosSingleSignOnExtension, MacOSRedirectSingleSignOnExtension]] = Field(alias="macOSSingleSignOnExtension", default=None,discriminator="odata_type", )
	powerOffDisabledWhileLoggedIn: Optional[bool] = Field(alias="powerOffDisabledWhileLoggedIn", default=None,)
	restartDisabled: Optional[bool] = Field(alias="restartDisabled", default=None,)
	restartDisabledWhileLoggedIn: Optional[bool] = Field(alias="restartDisabledWhileLoggedIn", default=None,)
	screenLockDisableImmediate: Optional[bool] = Field(alias="screenLockDisableImmediate", default=None,)
	shutDownDisabled: Optional[bool] = Field(alias="shutDownDisabled", default=None,)
	shutDownDisabledWhileLoggedIn: Optional[bool] = Field(alias="shutDownDisabledWhileLoggedIn", default=None,)
	singleSignOnExtension: Optional[Union[CredentialSingleSignOnExtension, IosSingleSignOnExtension, IosAzureAdSingleSignOnExtension, IosCredentialSingleSignOnExtension, IosKerberosSingleSignOnExtension, IosRedirectSingleSignOnExtension, KerberosSingleSignOnExtension, MacOSSingleSignOnExtension, MacOSAzureAdSingleSignOnExtension, MacOSCredentialSingleSignOnExtension, MacOSKerberosSingleSignOnExtension, MacOSRedirectSingleSignOnExtension, RedirectSingleSignOnExtension]] = Field(alias="singleSignOnExtension", default=None,discriminator="odata_type", )
	sleepDisabled: Optional[bool] = Field(alias="sleepDisabled", default=None,)
	singleSignOnExtensionPkinitCertificate: Optional[Union[MacOSImportedPFXCertificateProfile, MacOSPkcsCertificateProfile, MacOSScepCertificateProfile]] = Field(alias="singleSignOnExtensionPkinitCertificate", default=None,discriminator="odata_type", )

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
from .mac_o_s_associated_domains_item import MacOSAssociatedDomainsItem
from .key_value_pair import KeyValuePair
from .mac_o_s_launch_item import MacOSLaunchItem
from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range
from .mac_o_s_content_caching_client_policy import MacOSContentCachingClientPolicy
from .mac_o_s_content_caching_parent_selection_policy import MacOSContentCachingParentSelectionPolicy
from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range
from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range
from .mac_o_s_content_caching_peer_policy import MacOSContentCachingPeerPolicy
from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range
from .mac_o_s_content_caching_type import MacOSContentCachingType
from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
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
from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

