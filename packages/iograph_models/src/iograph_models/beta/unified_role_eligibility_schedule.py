from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UnifiedRoleEligibilitySchedule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleEligibilitySchedule"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleEligibilitySchedule")
	appScopeId: Optional[str] = Field(alias="appScopeId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	createdUsing: Optional[str] = Field(alias="createdUsing", default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	appScope: Optional[Union[CustomAppScope]] = Field(alias="appScope", default=None,discriminator="odata_type", )
	directoryScope: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User]] = Field(alias="directoryScope", default=None,discriminator="odata_type", )
	principal: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, CertificateAuthorityDetail, CertificateBasedAuthPki, Contract, Device, DeviceTemplate, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, DirectorySettingTemplate, Endpoint, ExtensionProperty, ExternalUserProfile, PendingExternalUserProfile, FederatedTokenValidationPolicy, Group, Mailbox, MultiTenantOrganizationMember, Organization, OrgContact, PermissionGrantPreApprovalPolicy, AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, CertificateBasedApplicationConfiguration, MutualTlsOauthConfiguration, User]] = Field(alias="principal", default=None,discriminator="odata_type", )
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition", default=None,)
	memberType: Optional[str] = Field(alias="memberType", default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo", default=None,)

from .custom_app_scope import CustomAppScope
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
from .org_contact import OrgContact
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
from .unified_role_definition import UnifiedRoleDefinition
from .request_schedule import RequestSchedule
