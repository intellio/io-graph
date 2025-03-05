from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchAnswerKeyword(BaseModel):
	keywords: Optional[list[str]] = Field(alias="keywords",default=None,)
	matchSimilarKeywords: Optional[bool] = Field(alias="matchSimilarKeywords",default=None,)
	reservedKeywords: Optional[list[str]] = Field(alias="reservedKeywords",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


