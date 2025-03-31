from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UnifiedRoleEligibilityScheduleRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleEligibilityScheduleRequest"] = Field(alias="@odata.type",)
	approvalId: Optional[str] = Field(alias="approvalId", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customData: Optional[str] = Field(alias="customData", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	action: Optional[UnifiedRoleScheduleRequestActions | str] = Field(alias="action", default=None,)
	appScopeId: Optional[str] = Field(alias="appScopeId", default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId", default=None,)
	isValidationOnly: Optional[bool] = Field(alias="isValidationOnly", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo", default=None,)
	targetScheduleId: Optional[str] = Field(alias="targetScheduleId", default=None,)
	ticketInfo: Optional[TicketInfo] = Field(alias="ticketInfo", default=None,)
	appScope: Optional[AppScope] = Field(alias="appScope", default=None,)
	directoryScope: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="directoryScope", default=None,discriminator="odata_type", )
	principal: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="principal", default=None,discriminator="odata_type", )
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition", default=None,)
	targetSchedule: Optional[UnifiedRoleEligibilitySchedule] = Field(alias="targetSchedule", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions
from .request_schedule import RequestSchedule
from .ticket_info import TicketInfo
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
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
