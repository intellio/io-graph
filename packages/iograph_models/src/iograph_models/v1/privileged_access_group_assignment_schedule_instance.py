from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PrivilegedAccessGroupAssignmentScheduleInstance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance")
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	accessId: Optional[PrivilegedAccessGroupRelationships | str] = Field(alias="accessId", default=None,)
	assignmentScheduleId: Optional[str] = Field(alias="assignmentScheduleId", default=None,)
	assignmentType: Optional[PrivilegedAccessGroupAssignmentType | str] = Field(alias="assignmentType", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	memberType: Optional[PrivilegedAccessGroupMemberType | str] = Field(alias="memberType", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	activatedUsing: Optional[PrivilegedAccessGroupEligibilityScheduleInstance] = Field(alias="activatedUsing", default=None,)
	group: Optional[Group] = Field(alias="group", default=None,)
	principal: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="principal", default=None,discriminator="odata_type", )

from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
from .privileged_access_group_assignment_type import PrivilegedAccessGroupAssignmentType
from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
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
