from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddPostRequest(BaseModel):
	values: Optional[list[ConversationMember]] = Field(default=None,alias="values",)

from .conversation_member import ConversationMember

