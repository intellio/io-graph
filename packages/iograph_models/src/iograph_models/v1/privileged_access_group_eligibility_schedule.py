from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupEligibilitySchedule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedAccessGroupEligibilitySchedule"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedAccessGroupEligibilitySchedule")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	createdUsing: Optional[str] = Field(alias="createdUsing", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	accessId: Optional[PrivilegedAccessGroupRelationships | str] = Field(alias="accessId", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	memberType: Optional[PrivilegedAccessGroupMemberType | str] = Field(alias="memberType", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	group: Optional[Group] = Field(alias="group", default=None,)
	principal: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="principal", default=None,discriminator="odata_type", )

from .request_schedule import RequestSchedule
from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .group import Group
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
from .policy_base import PolicyBase
from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .sts_policy import StsPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .service_principal import ServicePrincipal
from .user import User

