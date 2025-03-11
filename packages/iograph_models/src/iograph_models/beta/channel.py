from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Channel(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived",default=None,)
	isFavoriteByDefault: Optional[bool] = Field(alias="isFavoriteByDefault",default=None,)
	layoutType: Optional[ChannelLayoutType | str] = Field(alias="layoutType",default=None,)
	membershipType: Optional[ChannelMembershipType | str] = Field(alias="membershipType",default=None,)
	moderationSettings: Optional[ChannelModerationSettings] = Field(alias="moderationSettings",default=None,)
	summary: Optional[ChannelSummary] = Field(alias="summary",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	allMembers: SerializeAsAny[Optional[list[ConversationMember]]] = Field(alias="allMembers",default=None,)
	filesFolder: Optional[DriveItem] = Field(alias="filesFolder",default=None,)
	members: SerializeAsAny[Optional[list[ConversationMember]]] = Field(alias="members",default=None,)
	messages: Optional[list[ChatMessage]] = Field(alias="messages",default=None,)
	planner: Optional[TeamsChannelPlanner] = Field(alias="planner",default=None,)
	sharedWithTeams: Optional[list[SharedWithChannelTeamInfo]] = Field(alias="sharedWithTeams",default=None,)
	tabs: Optional[list[TeamsTab]] = Field(alias="tabs",default=None,)

from .channel_layout_type import ChannelLayoutType
from .channel_membership_type import ChannelMembershipType
from .channel_moderation_settings import ChannelModerationSettings
from .channel_summary import ChannelSummary
from .conversation_member import ConversationMember
from .drive_item import DriveItem
from .conversation_member import ConversationMember
from .chat_message import ChatMessage
from .teams_channel_planner import TeamsChannelPlanner
from .shared_with_channel_team_info import SharedWithChannelTeamInfo
from .teams_tab import TeamsTab

