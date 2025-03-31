from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserConsentRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userConsentRequest"] = Field(alias="@odata.type",)
	approvalId: Optional[str] = Field(alias="approvalId", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customData: Optional[str] = Field(alias="customData", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	approval: Optional[Approval] = Field(alias="approval", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .approval import Approval
