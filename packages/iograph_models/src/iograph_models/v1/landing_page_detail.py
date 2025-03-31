from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class LandingPageDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.landingPageDetail"] = Field(alias="@odata.type",)
	content: Optional[str] = Field(alias="content", default=None,)
	isDefaultLangauge: Optional[bool] = Field(alias="isDefaultLangauge", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)

