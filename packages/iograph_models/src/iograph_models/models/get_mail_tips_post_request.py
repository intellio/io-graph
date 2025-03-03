from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_mail_tipsPostRequest(BaseModel):
	EmailAddresses: Optional[list[str]] = Field(default=None,alias="EmailAddresses",)
	MailTipsOptions: Optional[MailTipsType] = Field(default=None,alias="MailTipsOptions",)

from .mail_tips_type import MailTipsType

