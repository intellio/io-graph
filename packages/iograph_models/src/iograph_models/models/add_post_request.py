from __future__ import annotations
from pydantic import BaseModel, Field


class AddPostRequest(BaseModel):
	values: list[ConversationMember] = Field(alias="values",)

from .conversation_member import ConversationMember

