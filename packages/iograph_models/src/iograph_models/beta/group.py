from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Group(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	accessType: Optional[GroupAccessType | str] = Field(alias="accessType",default=None,)
	allowExternalSenders: Optional[bool] = Field(alias="allowExternalSenders",default=None,)
	assignedLabels: Optional[list[AssignedLabel]] = Field(alias="assignedLabels",default=None,)
	assignedLicenses: Optional[list[AssignedLicense]] = Field(alias="assignedLicenses",default=None,)
	autoSubscribeNewMembers: Optional[bool] = Field(alias="autoSubscribeNewMembers",default=None,)
	classification: Optional[str] = Field(alias="classification",default=None,)
	cloudLicensing: Optional[CloudLicensingGroupCloudLicensing] = Field(alias="cloudLicensing",default=None,)
	createdByAppId: Optional[str] = Field(alias="createdByAppId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	groupTypes: Optional[list[str]] = Field(alias="groupTypes",default=None,)
	hasMembersWithLicenseErrors: Optional[bool] = Field(alias="hasMembersWithLicenseErrors",default=None,)
	hideFromAddressLists: Optional[bool] = Field(alias="hideFromAddressLists",default=None,)
	hideFromOutlookClients: Optional[bool] = Field(alias="hideFromOutlookClients",default=None,)
	infoCatalogs: Optional[list[str]] = Field(alias="infoCatalogs",default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived",default=None,)
	isAssignableToRole: Optional[bool] = Field(alias="isAssignableToRole",default=None,)
	isFavorite: Optional[bool] = Field(alias="isFavorite",default=None,)
	isManagementRestricted: Optional[bool] = Field(alias="isManagementRestricted",default=None,)
	isSubscribedByMail: Optional[bool] = Field(alias="isSubscribedByMail",default=None,)
	licenseProcessingState: Optional[LicenseProcessingState] = Field(alias="licenseProcessingState",default=None,)
	mail: Optional[str] = Field(alias="mail",default=None,)
	mailEnabled: Optional[bool] = Field(alias="mailEnabled",default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname",default=None,)
	membershipRule: Optional[str] = Field(alias="membershipRule",default=None,)
	membershipRuleProcessingState: Optional[str] = Field(alias="membershipRuleProcessingState",default=None,)
	membershipRuleProcessingStatus: Optional[MembershipRuleProcessingStatus] = Field(alias="membershipRuleProcessingStatus",default=None,)
	onPremisesDomainName: Optional[str] = Field(alias="onPremisesDomainName",default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime",default=None,)
	onPremisesNetBiosName: Optional[str] = Field(alias="onPremisesNetBiosName",default=None,)
	onPremisesProvisioningErrors: Optional[list[OnPremisesProvisioningError]] = Field(alias="onPremisesProvisioningErrors",default=None,)
	onPremisesSamAccountName: Optional[str] = Field(alias="onPremisesSamAccountName",default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier",default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled",default=None,)
	organizationId: Optional[str] = Field(alias="organizationId",default=None,)
	preferredDataLocation: Optional[str] = Field(alias="preferredDataLocation",default=None,)
	preferredLanguage: Optional[str] = Field(alias="preferredLanguage",default=None,)
	proxyAddresses: Optional[list[str]] = Field(alias="proxyAddresses",default=None,)
	renewedDateTime: Optional[datetime] = Field(alias="renewedDateTime",default=None,)
	resourceBehaviorOptions: Optional[list[str]] = Field(alias="resourceBehaviorOptions",default=None,)
	resourceProvisioningOptions: Optional[list[str]] = Field(alias="resourceProvisioningOptions",default=None,)
	securityEnabled: Optional[bool] = Field(alias="securityEnabled",default=None,)
	securityIdentifier: Optional[str] = Field(alias="securityIdentifier",default=None,)
	serviceProvisioningErrors: SerializeAsAny[Optional[list[ServiceProvisioningError]]] = Field(alias="serviceProvisioningErrors",default=None,)
	theme: Optional[str] = Field(alias="theme",default=None,)
	uniqueName: Optional[str] = Field(alias="uniqueName",default=None,)
	unseenConversationsCount: Optional[int] = Field(alias="unseenConversationsCount",default=None,)
	unseenCount: Optional[int] = Field(alias="unseenCount",default=None,)
	unseenMessagesCount: Optional[int] = Field(alias="unseenMessagesCount",default=None,)
	visibility: Optional[str] = Field(alias="visibility",default=None,)
	writebackConfiguration: Optional[GroupWritebackConfiguration] = Field(alias="writebackConfiguration",default=None,)
	acceptedSenders: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="acceptedSenders",default=None,)
	appRoleAssignments: Optional[list[AppRoleAssignment]] = Field(alias="appRoleAssignments",default=None,)
	calendar: Optional[Calendar] = Field(alias="calendar",default=None,)
	calendarView: Optional[list[Event]] = Field(alias="calendarView",default=None,)
	conversations: Optional[list[Conversation]] = Field(alias="conversations",default=None,)
	createdOnBehalfOf: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="createdOnBehalfOf",default=None,)
	drive: Optional[Drive] = Field(alias="drive",default=None,)
	drives: Optional[list[Drive]] = Field(alias="drives",default=None,)
	endpoints: Optional[list[Endpoint]] = Field(alias="endpoints",default=None,)
	events: Optional[list[Event]] = Field(alias="events",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	groupLifecyclePolicies: Optional[list[GroupLifecyclePolicy]] = Field(alias="groupLifecyclePolicies",default=None,)
	memberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="memberOf",default=None,)
	members: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="members",default=None,)
	membersWithLicenseErrors: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="membersWithLicenseErrors",default=None,)
	onenote: Optional[Onenote] = Field(alias="onenote",default=None,)
	owners: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="owners",default=None,)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="permissionGrants",default=None,)
	photo: Optional[ProfilePhoto] = Field(alias="photo",default=None,)
	photos: Optional[list[ProfilePhoto]] = Field(alias="photos",default=None,)
	planner: Optional[PlannerGroup] = Field(alias="planner",default=None,)
	rejectedSenders: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="rejectedSenders",default=None,)
	settings: Optional[list[DirectorySetting]] = Field(alias="settings",default=None,)
	sites: Optional[list[Site]] = Field(alias="sites",default=None,)
	team: Optional[Team] = Field(alias="team",default=None,)
	threads: Optional[list[ConversationThread]] = Field(alias="threads",default=None,)
	transitiveMemberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="transitiveMemberOf",default=None,)
	transitiveMembers: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="transitiveMembers",default=None,)

from .group_access_type import GroupAccessType
from .assigned_label import AssignedLabel
from .assigned_license import AssignedLicense
from .cloud_licensing_group_cloud_licensing import CloudLicensingGroupCloudLicensing
from .license_processing_state import LicenseProcessingState
from .membership_rule_processing_status import MembershipRuleProcessingStatus
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .service_provisioning_error import ServiceProvisioningError
from .group_writeback_configuration import GroupWritebackConfiguration
from .directory_object import DirectoryObject
from .app_role_assignment import AppRoleAssignment
from .calendar import Calendar
from .event import Event
from .conversation import Conversation
from .directory_object import DirectoryObject
from .drive import Drive
from .drive import Drive
from .endpoint import Endpoint
from .event import Event
from .extension import Extension
from .group_lifecycle_policy import GroupLifecyclePolicy
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .onenote import Onenote
from .directory_object import DirectoryObject
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .profile_photo import ProfilePhoto
from .profile_photo import ProfilePhoto
from .planner_group import PlannerGroup
from .directory_object import DirectoryObject
from .directory_setting import DirectorySetting
from .site import Site
from .team import Team
from .conversation_thread import ConversationThread
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

