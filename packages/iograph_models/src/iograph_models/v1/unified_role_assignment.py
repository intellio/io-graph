from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class UnifiedRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleAssignment")
	appScopeId: Optional[str] = Field(alias="appScopeId", default=None,)
	condition: Optional[str] = Field(alias="condition", default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	appScope: Optional[AppScope] = Field(alias="appScope", default=None,)
	directoryScope: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="directoryScope", default=None,discriminator="odata_type", )
	principal: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="principal", default=None,discriminator="odata_type", )
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition", default=None,)

from .app_scope import AppScope
from .administrative_unit import AdministrativeUnit
from .application import Application
from .app_role_assignment import AppRoleAssignment
from .contract import Contract
from .device import Device
from .directory_object_partner_reference import DirectoryObjectPartnerReference
from .directory_role import DirectoryRole
from .directory_role_template import DirectoryRoleTemplate
from .endpoint import Endpoint
from .extension_property import ExtensionProperty
from .group import Group
from .group_setting_template import GroupSettingTemplate
from .multi_tenant_organization_member import MultiTenantOrganizationMember
from .organization import Organization
from .org_contact import OrgContact
from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .service_principal import ServicePrincipal
from .user import User
from .unified_role_definition import UnifiedRoleDefinition
