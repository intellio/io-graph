from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TrainingLanguageDetail(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	content: Optional[str] = Field(default=None,alias="content",)
	createdBy: Optional[EmailIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isDefaultLangauge: Optional[bool] = Field(default=None,alias="isDefaultLangauge",)
	lastModifiedBy: Optional[EmailIdentity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	locale: Optional[str] = Field(default=None,alias="locale",)

from .email_identity import EmailIdentity
from .email_identity import EmailIdentity

