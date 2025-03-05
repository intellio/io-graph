from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_mail_tipsPostRequest(BaseModel):
	EmailAddresses: Optional[list[str]] = Field(alias="EmailAddresses",default=None,)
	MailTipsOptions: Optional[MailTipsType | str] = Field(alias="MailTipsOptions",default=None,)

from .mail_tips_type import MailTipsType

