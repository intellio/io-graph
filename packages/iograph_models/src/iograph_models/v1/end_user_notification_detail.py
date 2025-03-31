from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EndUserNotificationDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.endUserNotificationDetail"] = Field(alias="@odata.type",)
	emailContent: Optional[str] = Field(alias="emailContent", default=None,)
	isDefaultLangauge: Optional[bool] = Field(alias="isDefaultLangauge", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	sentFrom: Optional[EmailIdentity] = Field(alias="sentFrom", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)

from .email_identity import EmailIdentity
