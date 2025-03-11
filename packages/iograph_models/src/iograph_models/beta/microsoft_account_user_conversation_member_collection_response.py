from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAccountUserConversationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MicrosoftAccountUserConversationMember]] = Field(alias="value",default=None,)

from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember

