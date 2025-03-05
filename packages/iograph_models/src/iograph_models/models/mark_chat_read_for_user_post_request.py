from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Mark_chat_read_for_userPostRequest(BaseModel):
	user: Optional[TeamworkUserIdentity] = Field(alias="user",default=None,)

from .teamwork_user_identity import TeamworkUserIdentity

