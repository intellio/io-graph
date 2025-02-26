from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricLevelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RubricLevel] = Field(alias="value",)

from .rubric_level import RubricLevel

