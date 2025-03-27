from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExchangeAdmin(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	mailboxes: Optional[list[Mailbox]] = Field(alias="mailboxes", default=None,)
	messageTraces: Optional[list[MessageTrace]] = Field(alias="messageTraces", default=None,)

from .mailbox import Mailbox
from .message_trace import MessageTrace

