from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class VirtualEventPresenterInfo(BaseModel):
	identity: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="identity", default=None,discriminator="odata_type", )
	role: Optional[OnlineMeetingRole | str] = Field(alias="role", default=None,)
	upn: Optional[str] = Field(alias="upn", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEventPresenterInfo"] = Field(alias="@odata.type", default="#microsoft.graph.virtualEventPresenterInfo")
	presenterDetails: Optional[VirtualEventPresenterDetails] = Field(alias="presenterDetails", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .online_meeting_role import OnlineMeetingRole
from .virtual_event_presenter_details import VirtualEventPresenterDetails
