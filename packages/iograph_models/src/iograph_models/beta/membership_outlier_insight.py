from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MembershipOutlierInsight(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.membershipOutlierInsight"] = Field(alias="@odata.type", default="#microsoft.graph.membershipOutlierInsight")
	insightCreatedDateTime: Optional[datetime] = Field(alias="insightCreatedDateTime", default=None,)
	containerId: Optional[str] = Field(alias="containerId", default=None,)
	memberId: Optional[str] = Field(alias="memberId", default=None,)
	outlierContainerType: Optional[OutlierContainerType | str] = Field(alias="outlierContainerType", default=None,)
	outlierMemberType: Optional[OutlierMemberType | str] = Field(alias="outlierMemberType", default=None,)
	container: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalProfile, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, PolicyBase, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, TenantRelationshipAccessPolicyBase, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, TrustedCertificateAuthorityAsEntityBase, CertificateBasedApplicationConfiguration, TrustedCertificateAuthorityBase, MutualTlsOauthConfiguration, User]] = Field(alias="container", default=None,discriminator="odata_type", )
	lastModifiedBy: Optional[User] = Field(alias="lastModifiedBy", default=None,)
	member: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalProfile, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, PolicyBase, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, TenantRelationshipAccessPolicyBase, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, TrustedCertificateAuthorityAsEntityBase, CertificateBasedApplicationConfiguration, TrustedCertificateAuthorityBase, MutualTlsOauthConfiguration, User]] = Field(alias="member", default=None,discriminator="odata_type", )

from .outlier_container_type import OutlierContainerType
from .outlier_member_type import OutlierMemberType
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
from .user import User
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

