from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LandingPageDetail(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	isDefaultLangauge: Optional[bool] = Field(alias="isDefaultLangauge",default=None,)
	language: Optional[str] = Field(alias="language",default=None,)


