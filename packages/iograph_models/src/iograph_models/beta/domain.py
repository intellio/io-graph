from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Domain(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authenticationType: Optional[str] = Field(alias="authenticationType", default=None,)
	availabilityStatus: Optional[str] = Field(alias="availabilityStatus", default=None,)
	isAdminManaged: Optional[bool] = Field(alias="isAdminManaged", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isInitial: Optional[bool] = Field(alias="isInitial", default=None,)
	isRoot: Optional[bool] = Field(alias="isRoot", default=None,)
	isVerified: Optional[bool] = Field(alias="isVerified", default=None,)
	passwordNotificationWindowInDays: Optional[int] = Field(alias="passwordNotificationWindowInDays", default=None,)
	passwordValidityPeriodInDays: Optional[int] = Field(alias="passwordValidityPeriodInDays", default=None,)
	state: Optional[DomainState] = Field(alias="state", default=None,)
	supportedServices: Optional[list[str]] = Field(alias="supportedServices", default=None,)
	domainNameReferences: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalProfile, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, PolicyBase, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, TenantRelationshipAccessPolicyBase, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, TrustedCertificateAuthorityAsEntityBase, CertificateBasedApplicationConfiguration, TrustedCertificateAuthorityBase, MutualTlsOauthConfiguration, User]],Field(discriminator="odata_type")]]] = Field(alias="domainNameReferences", default=None,)
	federationConfiguration: Optional[list[InternalDomainFederation]] = Field(alias="federationConfiguration", default=None,)
	rootDomain: Optional[Domain] = Field(alias="rootDomain", default=None,)
	serviceConfigurationRecords: Optional[list[Annotated[Union[DomainDnsCnameRecord, DomainDnsMxRecord, DomainDnsSrvRecord, DomainDnsTxtRecord, DomainDnsUnavailableRecord]],Field(discriminator="odata_type")]]] = Field(alias="serviceConfigurationRecords", default=None,)
	sharedEmailDomainInvitations: Optional[list[SharedEmailDomainInvitation]] = Field(alias="sharedEmailDomainInvitations", default=None,)
	verificationDnsRecords: Optional[list[Annotated[Union[DomainDnsCnameRecord, DomainDnsMxRecord, DomainDnsSrvRecord, DomainDnsTxtRecord, DomainDnsUnavailableRecord]],Field(discriminator="odata_type")]]] = Field(alias="verificationDnsRecords", default=None,)

from .domain_state import DomainState
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
from .external_profile import ExternalProfile
from .external_user_profile import ExternalUserProfile
from .pending_external_user_profile import PendingExternalUserProfile
from .federated_token_validation_policy import FederatedTokenValidationPolicy
from .group import Group
from .mailbox import Mailbox
from .multi_tenant_organization_member import MultiTenantOrganizationMember
from .organization import Organization
from .org_contact import OrgContact
from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
from .policy_base import PolicyBase
from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .external_identities_policy import ExternalIdentitiesPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .service_principal_creation_policy import ServicePrincipalCreationPolicy
from .sts_policy import StsPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .service_principal import ServicePrincipal
from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase
from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase
from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
from .user import User
from .internal_domain_federation import InternalDomainFederation
from .domain_dns_cname_record import DomainDnsCnameRecord
from .domain_dns_mx_record import DomainDnsMxRecord
from .domain_dns_srv_record import DomainDnsSrvRecord
from .domain_dns_txt_record import DomainDnsTxtRecord
from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
from .shared_email_domain_invitation import SharedEmailDomainInvitation
from .domain_dns_cname_record import DomainDnsCnameRecord
from .domain_dns_mx_record import DomainDnsMxRecord
from .domain_dns_srv_record import DomainDnsSrvRecord
from .domain_dns_txt_record import DomainDnsTxtRecord
from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

