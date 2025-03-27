from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Chat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	chatType: Optional[ChatType | str] = Field(alias="chatType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isHiddenForAllMembers: Optional[bool] = Field(alias="isHiddenForAllMembers", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	onlineMeetingInfo: Optional[TeamworkOnlineMeetingInfo] = Field(alias="onlineMeetingInfo", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	topic: Optional[str] = Field(alias="topic", default=None,)
	viewpoint: Optional[ChatViewpoint] = Field(alias="viewpoint", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	installedApps: Optional[list[Annotated[Union[UserScopeTeamsAppInstallation]],Field(discriminator="odata_type")]]] = Field(alias="installedApps", default=None,)
	lastMessagePreview: Optional[ChatMessageInfo] = Field(alias="lastMessagePreview", default=None,)
	members: Optional[list[Annotated[Union[AadUserConversationMember, AnonymousGuestConversationMember, AzureCommunicationServicesUserConversationMember, MicrosoftAccountUserConversationMember, SkypeForBusinessUserConversationMember, SkypeUserConversationMember]],Field(discriminator="odata_type")]]] = Field(alias="members", default=None,)
	messages: Optional[list[ChatMessage]] = Field(alias="messages", default=None,)
	permissionGrants: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="permissionGrants", default=None,)
	pinnedMessages: Optional[list[PinnedChatMessageInfo]] = Field(alias="pinnedMessages", default=None,)
	tabs: Optional[list[TeamsTab]] = Field(alias="tabs", default=None,)

from .chat_type import ChatType
from .teamwork_online_meeting_info import TeamworkOnlineMeetingInfo
from .chat_viewpoint import ChatViewpoint
from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
from .chat_message_info import ChatMessageInfo
from .aad_user_conversation_member import AadUserConversationMember
from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
from .skype_user_conversation_member import SkypeUserConversationMember
from .chat_message import ChatMessage
from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
from .pinned_chat_message_info import PinnedChatMessageInfo
from .teams_tab import TeamsTab

