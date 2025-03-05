from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LandingPageDetail(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	content: Optional[str] = Field(default=None,alias="content",)
	isDefaultLangauge: Optional[bool] = Field(default=None,alias="isDefaultLangauge",)
	language: Optional[str] = Field(default=None,alias="language",)


