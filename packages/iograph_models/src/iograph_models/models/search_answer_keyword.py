from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchAnswerKeyword(BaseModel):
	keywords: Optional[list[str]] = Field(default=None,alias="keywords",)
	matchSimilarKeywords: Optional[bool] = Field(default=None,alias="matchSimilarKeywords",)
	reservedKeywords: Optional[list[str]] = Field(default=None,alias="reservedKeywords",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


