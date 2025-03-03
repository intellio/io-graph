from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Create_replyPostRequest(BaseModel):
	Message: Optional[Message] = Field(default=None,alias="Message",)
	Comment: Optional[str] = Field(default=None,alias="Comment",)

from .message import Message

