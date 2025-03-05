from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvitedUserMessageInfo(BaseModel):
	ccRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(default=None,alias="ccRecipients",)
	customizedMessageBody: Optional[str] = Field(default=None,alias="customizedMessageBody",)
	messageLanguage: Optional[str] = Field(default=None,alias="messageLanguage",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recipient import Recipient

