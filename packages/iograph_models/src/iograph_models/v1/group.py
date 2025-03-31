from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class Group(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.group"] = Field(alias="@odata.type", default="#microsoft.graph.group")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	allowExternalSenders: Optional[bool] = Field(alias="allowExternalSenders", default=None,)
	assignedLabels: Optional[list[AssignedLabel]] = Field(alias="assignedLabels", default=None,)
	assignedLicenses: Optional[list[AssignedLicense]] = Field(alias="assignedLicenses", default=None,)
	autoSubscribeNewMembers: Optional[bool] = Field(alias="autoSubscribeNewMembers", default=None,)
	classification: Optional[str] = Field(alias="classification", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	groupTypes: Optional[list[str]] = Field(alias="groupTypes", default=None,)
	hasMembersWithLicenseErrors: Optional[bool] = Field(alias="hasMembersWithLicenseErrors", default=None,)
	hideFromAddressLists: Optional[bool] = Field(alias="hideFromAddressLists", default=None,)
	hideFromOutlookClients: Optional[bool] = Field(alias="hideFromOutlookClients", default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived", default=None,)
	isAssignableToRole: Optional[bool] = Field(alias="isAssignableToRole", default=None,)
	isManagementRestricted: Optional[bool] = Field(alias="isManagementRestricted", default=None,)
	isSubscribedByMail: Optional[bool] = Field(alias="isSubscribedByMail", default=None,)
	licenseProcessingState: Optional[LicenseProcessingState] = Field(alias="licenseProcessingState", default=None,)
	mail: Optional[str] = Field(alias="mail", default=None,)
	mailEnabled: Optional[bool] = Field(alias="mailEnabled", default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname", default=None,)
	membershipRule: Optional[str] = Field(alias="membershipRule", default=None,)
	membershipRuleProcessingState: Optional[str] = Field(alias="membershipRuleProcessingState", default=None,)
	onPremisesDomainName: Optional[str] = Field(alias="onPremisesDomainName", default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime", default=None,)
	onPremisesNetBiosName: Optional[str] = Field(alias="onPremisesNetBiosName", default=None,)
	onPremisesProvisioningErrors: Optional[list[OnPremisesProvisioningError]] = Field(alias="onPremisesProvisioningErrors", default=None,)
	onPremisesSamAccountName: Optional[str] = Field(alias="onPremisesSamAccountName", default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier", default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled", default=None,)
	preferredDataLocation: Optional[str] = Field(alias="preferredDataLocation", default=None,)
	preferredLanguage: Optional[str] = Field(alias="preferredLanguage", default=None,)
	proxyAddresses: Optional[list[str]] = Field(alias="proxyAddresses", default=None,)
	renewedDateTime: Optional[datetime] = Field(alias="renewedDateTime", default=None,)
	securityEnabled: Optional[bool] = Field(alias="securityEnabled", default=None,)
	securityIdentifier: Optional[str] = Field(alias="securityIdentifier", default=None,)
	serviceProvisioningErrors: Optional[list[Annotated[Union[ServiceProvisioningXmlError],Field(discriminator="odata_type")]]] = Field(alias="serviceProvisioningErrors", default=None,)
	theme: Optional[str] = Field(alias="theme", default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName", default=None,)
	unseenCount: Optional[int] = Field(alias="unseenCount", default=None,)
	visibility: Optional[str] = Field(alias="visibility", default=None,)
	acceptedSenders: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="acceptedSenders", default=None,)
	appRoleAssignments: Optional[list[AppRoleAssignment]] = Field(alias="appRoleAssignments", default=None,)
	calendar: Optional[Calendar] = Field(alias="calendar", default=None,)
	calendarView: Optional[list[Event]] = Field(alias="calendarView", default=None,)
	conversations: Optional[list[Conversation]] = Field(alias="conversations", default=None,)
	createdOnBehalfOf: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="createdOnBehalfOf", default=None,discriminator="odata_type", )
	drive: Optional[Drive] = Field(alias="drive", default=None,)
	drives: Optional[list[Drive]] = Field(alias="drives", default=None,)
	events: Optional[list[Event]] = Field(alias="events", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	groupLifecyclePolicies: Optional[list[GroupLifecyclePolicy]] = Field(alias="groupLifecyclePolicies", default=None,)
	memberOf: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="memberOf", default=None,)
	members: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="members", default=None,)
	membersWithLicenseErrors: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="membersWithLicenseErrors", default=None,)
	onenote: Optional[Onenote] = Field(alias="onenote", default=None,)
	owners: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="owners", default=None,)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="permissionGrants", default=None,)
	photo: Optional[ProfilePhoto] = Field(alias="photo", default=None,)
	photos: Optional[list[ProfilePhoto]] = Field(alias="photos", default=None,)
	planner: Optional[PlannerGroup] = Field(alias="planner", default=None,)
	rejectedSenders: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="rejectedSenders", default=None,)
	settings: Optional[list[GroupSetting]] = Field(alias="settings", default=None,)
	sites: Optional[list[Site]] = Field(alias="sites", default=None,)
	team: Optional[Team] = Field(alias="team", default=None,)
	threads: Optional[list[ConversationThread]] = Field(alias="threads", default=None,)
	transitiveMemberOf: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="transitiveMemberOf", default=None,)
	transitiveMembers: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User],Field(discriminator="odata_type")]]] = Field(alias="transitiveMembers", default=None,)

from .assigned_label import AssignedLabel
from .assigned_license import AssignedLicense
from .license_processing_state import LicenseProcessingState
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .service_provisioning_xml_error import ServiceProvisioningXmlError
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
from .calendar import Calendar
from .event import Event
from .conversation import Conversation
from .drive import Drive
from .open_type_extension import OpenTypeExtension
from .group_lifecycle_policy import GroupLifecyclePolicy
from .onenote import Onenote
from .profile_photo import ProfilePhoto
from .planner_group import PlannerGroup
from .group_setting import GroupSetting
from .site import Site
from .team import Team
from .conversation_thread import ConversationThread
