from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Mark_chat_unread_for_userPostRequest(BaseModel):
	user: Optional[TeamworkUserIdentity] = Field(alias="user", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	lastMessageReadDateTime: Optional[datetime] = Field(alias="lastMessageReadDateTime", default=None,)

from .teamwork_user_identity import TeamworkUserIdentity
