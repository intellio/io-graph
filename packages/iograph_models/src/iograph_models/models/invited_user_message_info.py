from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InvitedUserMessageInfo(BaseModel):
	ccRecipients: list[Recipient] = Field(alias="ccRecipients",)
	customizedMessageBody: Optional[str] = Field(default=None,alias="customizedMessageBody",)
	messageLanguage: Optional[str] = Field(default=None,alias="messageLanguage",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recipient import Recipient

