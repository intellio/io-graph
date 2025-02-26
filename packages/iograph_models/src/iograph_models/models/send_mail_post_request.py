from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Send_mailPostRequest(BaseModel):
	Message: Optional[Message] = Field(default=None,alias="Message",)
	SaveToSentItems: Optional[bool] = Field(default=None,alias="SaveToSentItems",)

from .message import Message

