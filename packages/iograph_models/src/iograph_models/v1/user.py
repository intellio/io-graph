from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class User(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.user"] = Field(alias="@odata.type", default="#microsoft.graph.user")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	aboutMe: Optional[str] = Field(alias="aboutMe", default=None,)
	accountEnabled: Optional[bool] = Field(alias="accountEnabled", default=None,)
	ageGroup: Optional[str] = Field(alias="ageGroup", default=None,)
	assignedLicenses: Optional[list[AssignedLicense]] = Field(alias="assignedLicenses", default=None,)
	assignedPlans: Optional[list[AssignedPlan]] = Field(alias="assignedPlans", default=None,)
	authorizationInfo: Optional[AuthorizationInfo] = Field(alias="authorizationInfo", default=None,)
	birthday: Optional[datetime] = Field(alias="birthday", default=None,)
	businessPhones: Optional[list[str]] = Field(alias="businessPhones", default=None,)
	city: Optional[str] = Field(alias="city", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	consentProvidedForMinor: Optional[str] = Field(alias="consentProvidedForMinor", default=None,)
	country: Optional[str] = Field(alias="country", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creationType: Optional[str] = Field(alias="creationType", default=None,)
	customSecurityAttributes: Optional[CustomSecurityAttributeValue] = Field(alias="customSecurityAttributes", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	deviceEnrollmentLimit: Optional[int] = Field(alias="deviceEnrollmentLimit", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	employeeHireDate: Optional[datetime] = Field(alias="employeeHireDate", default=None,)
	employeeId: Optional[str] = Field(alias="employeeId", default=None,)
	employeeLeaveDateTime: Optional[datetime] = Field(alias="employeeLeaveDateTime", default=None,)
	employeeOrgData: Optional[EmployeeOrgData] = Field(alias="employeeOrgData", default=None,)
	employeeType: Optional[str] = Field(alias="employeeType", default=None,)
	externalUserState: Optional[str] = Field(alias="externalUserState", default=None,)
	externalUserStateChangeDateTime: Optional[datetime] = Field(alias="externalUserStateChangeDateTime", default=None,)
	faxNumber: Optional[str] = Field(alias="faxNumber", default=None,)
	givenName: Optional[str] = Field(alias="givenName", default=None,)
	hireDate: Optional[datetime] = Field(alias="hireDate", default=None,)
	identities: Optional[list[ObjectIdentity]] = Field(alias="identities", default=None,)
	imAddresses: Optional[list[str]] = Field(alias="imAddresses", default=None,)
	interests: Optional[list[str]] = Field(alias="interests", default=None,)
	isManagementRestricted: Optional[bool] = Field(alias="isManagementRestricted", default=None,)
	isResourceAccount: Optional[bool] = Field(alias="isResourceAccount", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	lastPasswordChangeDateTime: Optional[datetime] = Field(alias="lastPasswordChangeDateTime", default=None,)
	legalAgeGroupClassification: Optional[str] = Field(alias="legalAgeGroupClassification", default=None,)
	licenseAssignmentStates: Optional[list[LicenseAssignmentState]] = Field(alias="licenseAssignmentStates", default=None,)
	mail: Optional[str] = Field(alias="mail", default=None,)
	mailboxSettings: Optional[MailboxSettings] = Field(alias="mailboxSettings", default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname", default=None,)
	mobilePhone: Optional[str] = Field(alias="mobilePhone", default=None,)
	mySite: Optional[str] = Field(alias="mySite", default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation", default=None,)
	onPremisesDistinguishedName: Optional[str] = Field(alias="onPremisesDistinguishedName", default=None,)
	onPremisesDomainName: Optional[str] = Field(alias="onPremisesDomainName", default=None,)
	onPremisesExtensionAttributes: Optional[OnPremisesExtensionAttributes] = Field(alias="onPremisesExtensionAttributes", default=None,)
	onPremisesImmutableId: Optional[str] = Field(alias="onPremisesImmutableId", default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime", default=None,)
	onPremisesProvisioningErrors: Optional[list[OnPremisesProvisioningError]] = Field(alias="onPremisesProvisioningErrors", default=None,)
	onPremisesSamAccountName: Optional[str] = Field(alias="onPremisesSamAccountName", default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier", default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled", default=None,)
	onPremisesUserPrincipalName: Optional[str] = Field(alias="onPremisesUserPrincipalName", default=None,)
	otherMails: Optional[list[str]] = Field(alias="otherMails", default=None,)
	passwordPolicies: Optional[str] = Field(alias="passwordPolicies", default=None,)
	passwordProfile: Optional[PasswordProfile] = Field(alias="passwordProfile", default=None,)
	pastProjects: Optional[list[str]] = Field(alias="pastProjects", default=None,)
	postalCode: Optional[str] = Field(alias="postalCode", default=None,)
	preferredDataLocation: Optional[str] = Field(alias="preferredDataLocation", default=None,)
	preferredLanguage: Optional[str] = Field(alias="preferredLanguage", default=None,)
	preferredName: Optional[str] = Field(alias="preferredName", default=None,)
	print: Optional[UserPrint] = Field(alias="print", default=None,)
	provisionedPlans: Optional[list[ProvisionedPlan]] = Field(alias="provisionedPlans", default=None,)
	proxyAddresses: Optional[list[str]] = Field(alias="proxyAddresses", default=None,)
	responsibilities: Optional[list[str]] = Field(alias="responsibilities", default=None,)
	schools: Optional[list[str]] = Field(alias="schools", default=None,)
	securityIdentifier: Optional[str] = Field(alias="securityIdentifier", default=None,)
	serviceProvisioningErrors: Optional[list[Annotated[Union[ServiceProvisioningXmlError]],Field(discriminator="odata_type")]]] = Field(alias="serviceProvisioningErrors", default=None,)
	showInAddressList: Optional[bool] = Field(alias="showInAddressList", default=None,)
	signInActivity: Optional[SignInActivity] = Field(alias="signInActivity", default=None,)
	signInSessionsValidFromDateTime: Optional[datetime] = Field(alias="signInSessionsValidFromDateTime", default=None,)
	skills: Optional[list[str]] = Field(alias="skills", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	streetAddress: Optional[str] = Field(alias="streetAddress", default=None,)
	surname: Optional[str] = Field(alias="surname", default=None,)
	usageLocation: Optional[str] = Field(alias="usageLocation", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	userType: Optional[str] = Field(alias="userType", default=None,)
	activities: Optional[list[UserActivity]] = Field(alias="activities", default=None,)
	agreementAcceptances: Optional[list[AgreementAcceptance]] = Field(alias="agreementAcceptances", default=None,)
	appRoleAssignments: Optional[list[AppRoleAssignment]] = Field(alias="appRoleAssignments", default=None,)
	authentication: Optional[Authentication] = Field(alias="authentication", default=None,)
	calendar: Optional[Calendar] = Field(alias="calendar", default=None,)
	calendarGroups: Optional[list[CalendarGroup]] = Field(alias="calendarGroups", default=None,)
	calendars: Optional[list[Calendar]] = Field(alias="calendars", default=None,)
	calendarView: Optional[list[Event]] = Field(alias="calendarView", default=None,)
	chats: Optional[list[Chat]] = Field(alias="chats", default=None,)
	cloudClipboard: Optional[CloudClipboardRoot] = Field(alias="cloudClipboard", default=None,)
	contactFolders: Optional[list[ContactFolder]] = Field(alias="contactFolders", default=None,)
	contacts: Optional[list[Contact]] = Field(alias="contacts", default=None,)
	createdObjects: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="createdObjects", default=None,)
	deviceManagementTroubleshootingEvents: Optional[list[Annotated[Union[EnrollmentTroubleshootingEvent]],Field(discriminator="odata_type")]]] = Field(alias="deviceManagementTroubleshootingEvents", default=None,)
	directReports: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="directReports", default=None,)
	drive: Optional[Drive] = Field(alias="drive", default=None,)
	drives: Optional[list[Drive]] = Field(alias="drives", default=None,)
	employeeExperience: Optional[EmployeeExperienceUser] = Field(alias="employeeExperience", default=None,)
	events: Optional[list[Event]] = Field(alias="events", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension]],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	followedSites: Optional[list[Site]] = Field(alias="followedSites", default=None,)
	inferenceClassification: Optional[InferenceClassification] = Field(alias="inferenceClassification", default=None,)
	insights: Optional[ItemInsights] = Field(alias="insights", default=None,)
	joinedTeams: Optional[list[Team]] = Field(alias="joinedTeams", default=None,)
	licenseDetails: Optional[list[LicenseDetails]] = Field(alias="licenseDetails", default=None,)
	mailFolders: Optional[list[Annotated[Union[MailSearchFolder]],Field(discriminator="odata_type")]]] = Field(alias="mailFolders", default=None,)
	managedAppRegistrations: Optional[list[Annotated[Union[AndroidManagedAppRegistration, IosManagedAppRegistration]],Field(discriminator="odata_type")]]] = Field(alias="managedAppRegistrations", default=None,)
	managedDevices: Optional[list[ManagedDevice]] = Field(alias="managedDevices", default=None,)
	manager: Optional[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]] = Field(alias="manager", default=None,discriminator="odata_type", )
	memberOf: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="memberOf", default=None,)
	messages: Optional[list[Annotated[Union[CalendarSharingMessage, EventMessage, EventMessageRequest, EventMessageResponse]],Field(discriminator="odata_type")]]] = Field(alias="messages", default=None,)
	oauth2PermissionGrants: Optional[list[OAuth2PermissionGrant]] = Field(alias="oauth2PermissionGrants", default=None,)
	onenote: Optional[Onenote] = Field(alias="onenote", default=None,)
	onlineMeetings: Optional[list[OnlineMeeting]] = Field(alias="onlineMeetings", default=None,)
	outlook: Optional[OutlookUser] = Field(alias="outlook", default=None,)
	ownedDevices: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="ownedDevices", default=None,)
	ownedObjects: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="ownedObjects", default=None,)
	people: Optional[list[Person]] = Field(alias="people", default=None,)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="permissionGrants", default=None,)
	photo: Optional[ProfilePhoto] = Field(alias="photo", default=None,)
	photos: Optional[list[ProfilePhoto]] = Field(alias="photos", default=None,)
	planner: Optional[PlannerUser] = Field(alias="planner", default=None,)
	presence: Optional[Presence] = Field(alias="presence", default=None,)
	registeredDevices: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="registeredDevices", default=None,)
	scopedRoleMemberOf: Optional[list[ScopedRoleMembership]] = Field(alias="scopedRoleMemberOf", default=None,)
	settings: Optional[UserSettings] = Field(alias="settings", default=None,)
	solutions: Optional[UserSolutionRoot] = Field(alias="solutions", default=None,)
	sponsors: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="sponsors", default=None,)
	teamwork: Optional[UserTeamwork] = Field(alias="teamwork", default=None,)
	todo: Optional[Todo] = Field(alias="todo", default=None,)
	transitiveMemberOf: Optional[list[Annotated[Union[AdministrativeUnit, Application, AppRoleAssignment, Contract, Device, DirectoryObjectPartnerReference, DirectoryRole, DirectoryRoleTemplate, Endpoint, ExtensionProperty, Group, GroupSettingTemplate, MultiTenantOrganizationMember, Organization, OrgContact, PolicyBase, AppManagementPolicy, AuthorizationPolicy, CrossTenantAccessPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, StsPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, ResourceSpecificPermissionGrant, ServicePrincipal, User]],Field(discriminator="odata_type")]]] = Field(alias="transitiveMemberOf", default=None,)

from .assigned_license import AssignedLicense
from .assigned_plan import AssignedPlan
from .authorization_info import AuthorizationInfo
from .custom_security_attribute_value import CustomSecurityAttributeValue
from .employee_org_data import EmployeeOrgData
from .object_identity import ObjectIdentity
from .license_assignment_state import LicenseAssignmentState
from .mailbox_settings import MailboxSettings
from .on_premises_extension_attributes import OnPremisesExtensionAttributes
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .password_profile import PasswordProfile
from .user_print import UserPrint
from .provisioned_plan import ProvisionedPlan
from .service_provisioning_xml_error import ServiceProvisioningXmlError
from .sign_in_activity import SignInActivity
from .user_activity import UserActivity
from .agreement_acceptance import AgreementAcceptance
from .app_role_assignment import AppRoleAssignment
from .authentication import Authentication
from .calendar import Calendar
from .calendar_group import CalendarGroup
from .calendar import Calendar
from .event import Event
from .chat import Chat
from .cloud_clipboard_root import CloudClipboardRoot
from .contact_folder import ContactFolder
from .contact import Contact
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
from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
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
from .drive import Drive
from .drive import Drive
from .employee_experience_user import EmployeeExperienceUser
from .event import Event
from .open_type_extension import OpenTypeExtension
from .site import Site
from .inference_classification import InferenceClassification
from .item_insights import ItemInsights
from .team import Team
from .license_details import LicenseDetails
from .mail_search_folder import MailSearchFolder
from .android_managed_app_registration import AndroidManagedAppRegistration
from .ios_managed_app_registration import IosManagedAppRegistration
from .managed_device import ManagedDevice
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
from .calendar_sharing_message import CalendarSharingMessage
from .event_message import EventMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse
from .o_auth2_permission_grant import OAuth2PermissionGrant
from .onenote import Onenote
from .online_meeting import OnlineMeeting
from .outlook_user import OutlookUser
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
from .person import Person
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .profile_photo import ProfilePhoto
from .profile_photo import ProfilePhoto
from .planner_user import PlannerUser
from .presence import Presence
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
from .scoped_role_membership import ScopedRoleMembership
from .user_settings import UserSettings
from .user_solution_root import UserSolutionRoot
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
from .user_teamwork import UserTeamwork
from .todo import Todo
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

