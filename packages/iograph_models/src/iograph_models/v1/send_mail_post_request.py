from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Send_mailPostRequest(BaseModel):
	Message: SerializeAsAny[Optional[Message]] = Field(alias="Message",default=None,)
	SaveToSentItems: Optional[bool] = Field(alias="SaveToSentItems",default=None,)

from .message import Message

