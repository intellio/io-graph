from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class OrgContact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.orgContact"] = Field(alias="@odata.type", default="#microsoft.graph.orgContact")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	addresses: Optional[list[PhysicalOfficeAddress]] = Field(alias="addresses", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	givenName: Optional[str] = Field(alias="givenName", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	mail: Optional[str] = Field(alias="mail", default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname", default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime", default=None,)
	onPremisesProvisioningErrors: Optional[list[OnPremisesProvisioningError]] = Field(alias="onPremisesProvisioningErrors", default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled", default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones", default=None,)
	proxyAddresses: Optional[list[str]] = Field(alias="proxyAddresses", default=None,)
	serviceProvisioningErrors: Optional[list[Annotated[Union[ServiceProvisioningResourceError, ServiceProvisioningXmlError],Field(discriminator="odata_type")]]] = Field(alias="serviceProvisioningErrors", default=None,)
	surname: Optional[str] = Field(alias="surname", default=None,)
	directReports: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User],Field(discriminator="odata_type")]]] = Field(alias="directReports", default=None,)
	manager: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User]] = Field(alias="manager", default=None,discriminator="odata_type", )
	memberOf: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User],Field(discriminator="odata_type")]]] = Field(alias="memberOf", default=None,)
	transitiveMemberOf: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User],Field(discriminator="odata_type")]]] = Field(alias="transitiveMemberOf", default=None,)
	transitiveReports: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User],Field(discriminator="odata_type")]]] = Field(alias="transitiveReports", default=None,)

from .physical_office_address import PhysicalOfficeAddress
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .phone import Phone
from .service_provisioning_resource_error import ServiceProvisioningResourceError
from .service_provisioning_xml_error import ServiceProvisioningXmlError
from .administrative_unit import AdministrativeUnit
from .application import Application
from .app_role_assignment import AppRoleAssignment
from .certificate_authority_detail import CertificateAuthorityDetail
from .certificate_based_auth_pki import CertificateBasedAuthPki
from .contract import Contract
from .device import Device
from .device_template import DeviceTemplate
from .directory_object_partner_reference import DirectoryObjectPartnerReference
from .directory_role import DirectoryRole
from .directory_role_template import DirectoryRoleTemplate
from .directory_setting_template import DirectorySettingTemplate
from .endpoint import Endpoint
from .extension_property import ExtensionProperty
from .external_user_profile import ExternalUserProfile
from .pending_external_user_profile import PendingExternalUserProfile
from .federated_token_validation_policy import FederatedTokenValidationPolicy
from .group import Group
from .mailbox import Mailbox
from .multi_tenant_organization_member import MultiTenantOrganizationMember
from .organization import Organization
from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .external_identities_policy import ExternalIdentitiesPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .service_principal_creation_policy import ServicePrincipalCreationPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .service_principal import ServicePrincipal
from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
from .user import User
