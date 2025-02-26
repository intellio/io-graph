from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_mail_tipsPostRequest(BaseModel):
	EmailAddresses: list[str] = Field(alias="EmailAddresses",)
	MailTipsOptions: Optional[MailTipsType] = Field(default=None,alias="MailTipsOptions",)

from .mail_tips_type import MailTipsType

