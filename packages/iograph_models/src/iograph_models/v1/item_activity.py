from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ItemActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemActivity"] = Field(alias="@odata.type",)
	access: Optional[AccessAction] = Field(alias="access", default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime", default=None,)
	actor: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="actor", default=None,discriminator="odata_type", )
	driveItem: Optional[DriveItem] = Field(alias="driveItem", default=None,)

from .access_action import AccessAction
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .drive_item import DriveItem
