from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Team(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	classification: Optional[str] = Field(alias="classification",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	funSettings: Optional[TeamFunSettings] = Field(alias="funSettings",default=None,)
	guestSettings: Optional[TeamGuestSettings] = Field(alias="guestSettings",default=None,)
	internalId: Optional[str] = Field(alias="internalId",default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived",default=None,)
	memberSettings: Optional[TeamMemberSettings] = Field(alias="memberSettings",default=None,)
	messagingSettings: Optional[TeamMessagingSettings] = Field(alias="messagingSettings",default=None,)
	specialization: Optional[TeamSpecialization | str] = Field(alias="specialization",default=None,)
	summary: Optional[TeamSummary] = Field(alias="summary",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	visibility: Optional[TeamVisibilityType | str] = Field(alias="visibility",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	allChannels: Optional[list[Channel]] = Field(alias="allChannels",default=None,)
	channels: Optional[list[Channel]] = Field(alias="channels",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)
	incomingChannels: Optional[list[Channel]] = Field(alias="incomingChannels",default=None,)
	installedApps: SerializeAsAny[Optional[list[TeamsAppInstallation]]] = Field(alias="installedApps",default=None,)
	members: SerializeAsAny[Optional[list[ConversationMember]]] = Field(alias="members",default=None,)
	operations: Optional[list[TeamsAsyncOperation]] = Field(alias="operations",default=None,)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="permissionGrants",default=None,)
	photo: Optional[ProfilePhoto] = Field(alias="photo",default=None,)
	primaryChannel: Optional[Channel] = Field(alias="primaryChannel",default=None,)
	schedule: Optional[Schedule] = Field(alias="schedule",default=None,)
	tags: Optional[list[TeamworkTag]] = Field(alias="tags",default=None,)
	template: Optional[TeamsTemplate] = Field(alias="template",default=None,)

from .team_fun_settings import TeamFunSettings
from .team_guest_settings import TeamGuestSettings
from .team_member_settings import TeamMemberSettings
from .team_messaging_settings import TeamMessagingSettings
from .team_specialization import TeamSpecialization
from .team_summary import TeamSummary
from .team_visibility_type import TeamVisibilityType
from .channel import Channel
from .channel import Channel
from .group import Group
from .channel import Channel
from .teams_app_installation import TeamsAppInstallation
from .conversation_member import ConversationMember
from .teams_async_operation import TeamsAsyncOperation
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .profile_photo import ProfilePhoto
from .channel import Channel
from .schedule import Schedule
from .teamwork_tag import TeamworkTag
from .teams_template import TeamsTemplate

