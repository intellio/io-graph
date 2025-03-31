from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SkypeUserConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SkypeUserConversationMember]] = Field(alias="value", default=None,)

from .skype_user_conversation_member import SkypeUserConversationMember
