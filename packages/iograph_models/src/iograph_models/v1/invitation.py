from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Invitation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	invitedUserDisplayName: Optional[str] = Field(alias="invitedUserDisplayName", default=None,)
	invitedUserEmailAddress: Optional[str] = Field(alias="invitedUserEmailAddress", default=None,)
	invitedUserMessageInfo: Optional[InvitedUserMessageInfo] = Field(alias="invitedUserMessageInfo", default=None,)
	invitedUserType: Optional[str] = Field(alias="invitedUserType", default=None,)
	inviteRedeemUrl: Optional[str] = Field(alias="inviteRedeemUrl", default=None,)
	inviteRedirectUrl: Optional[str] = Field(alias="inviteRedirectUrl", default=None,)
	resetRedemption: Optional[bool] = Field(alias="resetRedemption", default=None,)
	sendInvitationMessage: Optional[bool] = Field(alias="sendInvitationMessage", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	invitedUser: Optional[User] = Field(alias="invitedUser", default=None,)
	invitedUserSponsors: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="invitedUserSponsors", default=None,)

from .invited_user_message_info import InvitedUserMessageInfo
from .user import User
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

