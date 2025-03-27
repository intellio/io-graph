from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AnonymousGuestConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AnonymousGuestConversationMember]] = Field(alias="value", default=None,)

from .anonymous_guest_conversation_member import AnonymousGuestConversationMember

