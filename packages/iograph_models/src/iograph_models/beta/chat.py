from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Chat(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	chatType: Optional[ChatType | str] = Field(alias="chatType",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	isHiddenForAllMembers: Optional[bool] = Field(alias="isHiddenForAllMembers",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	onlineMeetingInfo: Optional[TeamworkOnlineMeetingInfo] = Field(alias="onlineMeetingInfo",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	topic: Optional[str] = Field(alias="topic",default=None,)
	viewpoint: Optional[ChatViewpoint] = Field(alias="viewpoint",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	installedApps: SerializeAsAny[Optional[list[TeamsAppInstallation]]] = Field(alias="installedApps",default=None,)
	lastMessagePreview: Optional[ChatMessageInfo] = Field(alias="lastMessagePreview",default=None,)
	members: SerializeAsAny[Optional[list[ConversationMember]]] = Field(alias="members",default=None,)
	messages: Optional[list[ChatMessage]] = Field(alias="messages",default=None,)
	operations: Optional[list[TeamsAsyncOperation]] = Field(alias="operations",default=None,)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="permissionGrants",default=None,)
	pinnedMessages: Optional[list[PinnedChatMessageInfo]] = Field(alias="pinnedMessages",default=None,)
	tabs: Optional[list[TeamsTab]] = Field(alias="tabs",default=None,)

from .chat_type import ChatType
from .identity_set import IdentitySet
from .teamwork_online_meeting_info import TeamworkOnlineMeetingInfo
from .chat_viewpoint import ChatViewpoint
from .teams_app_installation import TeamsAppInstallation
from .chat_message_info import ChatMessageInfo
from .conversation_member import ConversationMember
from .chat_message import ChatMessage
from .teams_async_operation import TeamsAsyncOperation
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .pinned_chat_message_info import PinnedChatMessageInfo
from .teams_tab import TeamsTab

