from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Team(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	classification: Optional[str] = Field(default=None,alias="classification",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	funSettings: Optional[TeamFunSettings] = Field(default=None,alias="funSettings",)
	guestSettings: Optional[TeamGuestSettings] = Field(default=None,alias="guestSettings",)
	internalId: Optional[str] = Field(default=None,alias="internalId",)
	isArchived: Optional[bool] = Field(default=None,alias="isArchived",)
	memberSettings: Optional[TeamMemberSettings] = Field(default=None,alias="memberSettings",)
	messagingSettings: Optional[TeamMessagingSettings] = Field(default=None,alias="messagingSettings",)
	specialization: Optional[TeamSpecialization] = Field(default=None,alias="specialization",)
	summary: Optional[TeamSummary] = Field(default=None,alias="summary",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	visibility: Optional[TeamVisibilityType] = Field(default=None,alias="visibility",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	allChannels: Optional[list[Channel]] = Field(default=None,alias="allChannels",)
	channels: Optional[list[Channel]] = Field(default=None,alias="channels",)
	group: Optional[Group] = Field(default=None,alias="group",)
	incomingChannels: Optional[list[Channel]] = Field(default=None,alias="incomingChannels",)
	installedApps: Optional[list[TeamsAppInstallation]] = Field(default=None,alias="installedApps",)
	members: Optional[list[ConversationMember]] = Field(default=None,alias="members",)
	operations: Optional[list[TeamsAsyncOperation]] = Field(default=None,alias="operations",)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(default=None,alias="permissionGrants",)
	photo: Optional[ProfilePhoto] = Field(default=None,alias="photo",)
	primaryChannel: Optional[Channel] = Field(default=None,alias="primaryChannel",)
	schedule: Optional[Schedule] = Field(default=None,alias="schedule",)
	tags: Optional[list[TeamworkTag]] = Field(default=None,alias="tags",)
	template: Optional[TeamsTemplate] = Field(default=None,alias="template",)

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

