from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SkypeForBusinessUserConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SkypeForBusinessUserConversationMember]] = Field(default=None,alias="value",)

from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember

