from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchAnswerKeyword(BaseModel):
	keywords: list[Optional[str]] = Field(alias="keywords",)
	matchSimilarKeywords: Optional[bool] = Field(default=None,alias="matchSimilarKeywords",)
	reservedKeywords: list[Optional[str]] = Field(alias="reservedKeywords",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


