from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatRenamedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	chatDisplayName: Optional[str] = Field(default=None,alias="chatDisplayName",)
	chatId: Optional[str] = Field(default=None,alias="chatId",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)

from .identity_set import IdentitySet

