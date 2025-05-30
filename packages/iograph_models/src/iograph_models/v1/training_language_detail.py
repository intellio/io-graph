from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TrainingLanguageDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.trainingLanguageDetail"] = Field(alias="@odata.type", default="#microsoft.graph.trainingLanguageDetail")
	content: Optional[str] = Field(alias="content", default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDefaultLangauge: Optional[bool] = Field(alias="isDefaultLangauge", default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)

from .email_identity import EmailIdentity
