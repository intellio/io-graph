from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChallengingWord(BaseModel):
	count: Optional[int] = Field(alias="count", default=None,)
	word: Optional[str] = Field(alias="word", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

