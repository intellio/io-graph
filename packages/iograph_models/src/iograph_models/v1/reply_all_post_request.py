from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Reply_allPostRequest(BaseModel):
	Message: SerializeAsAny[Optional[Message]] = Field(alias="Message",default=None,)
	Comment: Optional[str] = Field(alias="Comment",default=None,)

from .message import Message

