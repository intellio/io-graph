from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DirectoryObjectCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

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
