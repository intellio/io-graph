from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MessageTrace(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.messageTrace"] = Field(alias="@odata.type", default="#microsoft.graph.messageTrace")
	destinationIPAddress: Optional[str] = Field(alias="destinationIPAddress", default=None,)
	messageId: Optional[str] = Field(alias="messageId", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	senderEmail: Optional[str] = Field(alias="senderEmail", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	sourceIPAddress: Optional[str] = Field(alias="sourceIPAddress", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	recipients: Optional[list[MessageRecipient]] = Field(alias="recipients", default=None,)

from .message_recipient import MessageRecipient
