from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeCard(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.timeCard"] = Field(alias="@odata.type", default="#microsoft.graph.timeCard")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	breaks: Optional[list[TimeCardBreak]] = Field(alias="breaks", default=None,)
	clockInEvent: Optional[TimeCardEvent] = Field(alias="clockInEvent", default=None,)
	clockOutEvent: Optional[TimeCardEvent] = Field(alias="clockOutEvent", default=None,)
	confirmedBy: Optional[ConfirmedBy | str] = Field(alias="confirmedBy", default=None,)
	notes: Optional[ItemBody] = Field(alias="notes", default=None,)
	originalEntry: Optional[TimeCardEntry] = Field(alias="originalEntry", default=None,)
	state: Optional[TimeCardState | str] = Field(alias="state", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .time_card_break import TimeCardBreak
from .time_card_event import TimeCardEvent
from .time_card_event import TimeCardEvent
from .confirmed_by import ConfirmedBy
from .item_body import ItemBody
from .time_card_entry import TimeCardEntry
from .time_card_state import TimeCardState

