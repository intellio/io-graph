from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatRenamedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	chatDisplayName: Optional[str] = Field(alias="chatDisplayName",default=None,)
	chatId: Optional[str] = Field(alias="chatId",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)

from .identity_set import IdentitySet

