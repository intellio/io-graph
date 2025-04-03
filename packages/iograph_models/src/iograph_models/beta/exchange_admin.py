from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExchangeAdmin(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exchangeAdmin"] = Field(alias="@odata.type", default="#microsoft.graph.exchangeAdmin")
	mailboxes: Optional[list[Mailbox]] = Field(alias="mailboxes", default=None,)
	messageTraces: Optional[list[MessageTrace]] = Field(alias="messageTraces", default=None,)

from .mailbox import Mailbox
from .message_trace import MessageTrace
