from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RemovePostRequest(BaseModel):
	values: SerializeAsAny[Optional[list[ConversationMember]]] = Field(alias="values",default=None,)

from .conversation_member import ConversationMember

