from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EndUserNotificationDetail(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	emailContent: Optional[str] = Field(alias="emailContent",default=None,)
	isDefaultLangauge: Optional[bool] = Field(alias="isDefaultLangauge",default=None,)
	language: Optional[str] = Field(alias="language",default=None,)
	locale: Optional[str] = Field(alias="locale",default=None,)
	sentFrom: Optional[EmailIdentity] = Field(alias="sentFrom",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)

from .email_identity import EmailIdentity

