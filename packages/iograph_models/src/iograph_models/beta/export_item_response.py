from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExportItemResponse(BaseModel):
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	data: Optional[str] = Field(alias="data", default=None,)
	error: Optional[MailTipsError] = Field(alias="error", default=None,)
	itemId: Optional[str] = Field(alias="itemId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .mail_tips_error import MailTipsError
