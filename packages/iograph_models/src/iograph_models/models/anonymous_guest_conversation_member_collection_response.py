from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AnonymousGuestConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AnonymousGuestConversationMember] = Field(alias="value",)

from .anonymous_guest_conversation_member import AnonymousGuestConversationMember

