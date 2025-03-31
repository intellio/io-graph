from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class Channel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.channel"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived", default=None,)
	isFavoriteByDefault: Optional[bool] = Field(alias="isFavoriteByDefault", default=None,)
	membershipType: Optional[ChannelMembershipType | str] = Field(alias="membershipType", default=None,)
	summary: Optional[ChannelSummary] = Field(alias="summary", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	allMembers: Optional[list[Annotated[Union[AadUserConversationMember, AnonymousGuestConversationMember, AzureCommunicationServicesUserConversationMember, MicrosoftAccountUserConversationMember, SkypeForBusinessUserConversationMember, SkypeUserConversationMember],Field(discriminator="odata_type")]]] = Field(alias="allMembers", default=None,)
	filesFolder: Optional[DriveItem] = Field(alias="filesFolder", default=None,)
	members: Optional[list[Annotated[Union[AadUserConversationMember, AnonymousGuestConversationMember, AzureCommunicationServicesUserConversationMember, MicrosoftAccountUserConversationMember, SkypeForBusinessUserConversationMember, SkypeUserConversationMember],Field(discriminator="odata_type")]]] = Field(alias="members", default=None,)
	messages: Optional[list[ChatMessage]] = Field(alias="messages", default=None,)
	sharedWithTeams: Optional[list[SharedWithChannelTeamInfo]] = Field(alias="sharedWithTeams", default=None,)
	tabs: Optional[list[TeamsTab]] = Field(alias="tabs", default=None,)

from .channel_membership_type import ChannelMembershipType
from .channel_summary import ChannelSummary
from .aad_user_conversation_member import AadUserConversationMember
from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
from .skype_user_conversation_member import SkypeUserConversationMember
from .drive_item import DriveItem
from .chat_message import ChatMessage
from .shared_with_channel_team_info import SharedWithChannelTeamInfo
from .teams_tab import TeamsTab
