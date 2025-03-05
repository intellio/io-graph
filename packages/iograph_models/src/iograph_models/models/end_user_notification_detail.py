from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EndUserNotificationDetail(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emailContent: Optional[str] = Field(default=None,alias="emailContent",)
	isDefaultLangauge: Optional[bool] = Field(default=None,alias="isDefaultLangauge",)
	language: Optional[str] = Field(default=None,alias="language",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	sentFrom: Optional[EmailIdentity] = Field(default=None,alias="sentFrom",)
	subject: Optional[str] = Field(default=None,alias="subject",)

from .email_identity import EmailIdentity

