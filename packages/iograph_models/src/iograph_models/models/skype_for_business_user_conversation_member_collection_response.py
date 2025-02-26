from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SkypeForBusinessUserConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SkypeForBusinessUserConversationMember] = Field(alias="value",)

from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember

