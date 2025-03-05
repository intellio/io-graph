from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Mark_chat_unread_for_userPostRequest(BaseModel):
	user: Optional[TeamworkUserIdentity] = Field(default=None,alias="user",)
	lastMessageReadDateTime: Optional[datetime] = Field(default=None,alias="lastMessageReadDateTime",)

from .teamwork_user_identity import TeamworkUserIdentity

