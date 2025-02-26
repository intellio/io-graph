from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkConversationIdentity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	conversationIdentityType: Optional[TeamworkConversationIdentityType] = Field(default=None,alias="conversationIdentityType",)

from .teamwork_conversation_identity_type import TeamworkConversationIdentityType

