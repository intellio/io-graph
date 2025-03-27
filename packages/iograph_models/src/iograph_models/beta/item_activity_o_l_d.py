from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActivityOLD(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	action: Optional[ItemActionSet] = Field(alias="action", default=None,)
	actor: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="actor", default=None,discriminator="odata_type", )
	times: Optional[ItemActivityTimeSet] = Field(alias="times", default=None,)
	driveItem: Optional[DriveItem] = Field(alias="driveItem", default=None,)
	listItem: Optional[ListItem] = Field(alias="listItem", default=None,)

from .item_action_set import ItemActionSet
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_activity_time_set import ItemActivityTimeSet
from .drive_item import DriveItem
from .list_item import ListItem

