from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ForwardPostRequest(BaseModel):
	ToRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(default=None,alias="ToRecipients",)
	Message: SerializeAsAny[Optional[Message]] = Field(default=None,alias="Message",)
	Comment: Optional[str] = Field(default=None,alias="Comment",)

from .recipient import Recipient
from .message import Message

