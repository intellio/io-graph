from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMembersNotificationRecipient(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	chatId: Optional[str] = Field(alias="chatId",default=None,)


