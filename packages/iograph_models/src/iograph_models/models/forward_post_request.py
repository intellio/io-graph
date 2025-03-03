from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ForwardPostRequest(BaseModel):
	ToRecipients: Optional[list[Recipient]] = Field(default=None,alias="ToRecipients",)
	Message: Optional[Message] = Field(default=None,alias="Message",)
	Comment: Optional[str] = Field(default=None,alias="Comment",)

from .recipient import Recipient
from .message import Message

