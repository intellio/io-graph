from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvitedUserMessageInfo(BaseModel):
	ccRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="ccRecipients",default=None,)
	customizedMessageBody: Optional[str] = Field(alias="customizedMessageBody",default=None,)
	messageLanguage: Optional[str] = Field(alias="messageLanguage",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .recipient import Recipient

