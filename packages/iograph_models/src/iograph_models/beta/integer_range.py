from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IntegerRange(BaseModel):
	end: Optional[int] = Field(alias="end", default=None,)
	maximum: Optional[int] = Field(alias="maximum", default=None,)
	minimum: Optional[int] = Field(alias="minimum", default=None,)
	start: Optional[int] = Field(alias="start", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

