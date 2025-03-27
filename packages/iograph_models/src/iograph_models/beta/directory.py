from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Directory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	administrativeUnits: Optional[list[AdministrativeUnit]] = Field(alias="administrativeUnits", default=None,)
	attributeSets: Optional[list[AttributeSet]] = Field(alias="attributeSets", default=None,)
	authenticationMethodDevices: Optional[Union[HardwareOathTokenAuthenticationMethodDevice]] = Field(alias="authenticationMethodDevices", default=None,discriminator="odata_type", )
	certificateAuthorities: Optional[CertificateAuthorityPath] = Field(alias="certificateAuthorities", default=None,)
	customSecurityAttributeDefinitions: Optional[list[CustomSecurityAttributeDefinition]] = Field(alias="customSecurityAttributeDefinitions", default=None,)
	deletedItems: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalProfile, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, PolicyBase, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, TenantRelationshipAccessPolicyBase, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, TrustedCertificateAuthorityAsEntityBase, CertificateBasedApplicationConfiguration, TrustedCertificateAuthorityBase, MutualTlsOauthConfiguration, User],Field(discriminator="odata_type")]]] = Field(alias="deletedItems", default=None,)
	deviceLocalCredentials: Optional[list[DeviceLocalCredentialInfo]] = Field(alias="deviceLocalCredentials", default=None,)
	externalUserProfiles: Optional[list[ExternalUserProfile]] = Field(alias="externalUserProfiles", default=None,)
	featureRolloutPolicies: Optional[list[FeatureRolloutPolicy]] = Field(alias="featureRolloutPolicies", default=None,)
	federationConfigurations: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, OidcIdentityProvider, OpenIdConnectIdentityProvider, SamlOrWsFedProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider],Field(discriminator="odata_type")]]] = Field(alias="federationConfigurations", default=None,)
	impactedResources: Optional[list[ImpactedResource]] = Field(alias="impactedResources", default=None,)
	inboundSharedUserProfiles: Optional[list[InboundSharedUserProfile]] = Field(alias="inboundSharedUserProfiles", default=None,)
	onPremisesSynchronization: Optional[list[OnPremisesDirectorySynchronization]] = Field(alias="onPremisesSynchronization", default=None,)
	outboundSharedUserProfiles: Optional[list[OutboundSharedUserProfile]] = Field(alias="outboundSharedUserProfiles", default=None,)
	pendingExternalUserProfiles: Optional[list[PendingExternalUserProfile]] = Field(alias="pendingExternalUserProfiles", default=None,)
	publicKeyInfrastructure: Optional[PublicKeyInfrastructureRoot] = Field(alias="publicKeyInfrastructure", default=None,)
	recommendations: Optional[list[Recommendation]] = Field(alias="recommendations", default=None,)
	sharedEmailDomains: Optional[list[SharedEmailDomain]] = Field(alias="sharedEmailDomains", default=None,)
	subscriptions: Optional[list[CompanySubscription]] = Field(alias="subscriptions", default=None,)
	templates: Optional[Template] = Field(alias="templates", default=None,)

from .administrative_unit import AdministrativeUnit
from .attribute_set import AttributeSet
from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice
from .certificate_authority_path import CertificateAuthorityPath
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
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
from .device_local_credential_info import DeviceLocalCredentialInfo
from .external_user_profile import ExternalUserProfile
from .feature_rollout_policy import FeatureRolloutPolicy
from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .oidc_identity_provider import OidcIdentityProvider
from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
from .saml_or_ws_fed_provider import SamlOrWsFedProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider
from .impacted_resource import ImpactedResource
from .inbound_shared_user_profile import InboundSharedUserProfile
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
from .outbound_shared_user_profile import OutboundSharedUserProfile
from .pending_external_user_profile import PendingExternalUserProfile
from .public_key_infrastructure_root import PublicKeyInfrastructureRoot
from .recommendation import Recommendation
from .shared_email_domain import SharedEmailDomain
from .company_subscription import CompanySubscription
from .template import Template

