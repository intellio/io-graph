from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AadUserConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AadUserConversationMember]] = Field(default=None,alias="value",)

from .aad_user_conversation_member import AadUserConversationMember

