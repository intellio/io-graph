from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamworkConversationIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkConversationIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.teamworkConversationIdentity")
	conversationIdentityType: Optional[TeamworkConversationIdentityType | str] = Field(alias="conversationIdentityType", default=None,)

from .teamwork_conversation_identity_type import TeamworkConversationIdentityType
