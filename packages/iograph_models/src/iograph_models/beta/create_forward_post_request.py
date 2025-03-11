from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_forwardPostRequest(BaseModel):
	ToRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="ToRecipients",default=None,)
	Message: SerializeAsAny[Optional[Message]] = Field(alias="Message",default=None,)
	Comment: Optional[str] = Field(alias="Comment",default=None,)

from .recipient import Recipient
from .message import Message

