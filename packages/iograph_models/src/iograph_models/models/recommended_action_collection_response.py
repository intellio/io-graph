from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecommendedActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RecommendedAction] = Field(alias="value",)

from .recommended_action import RecommendedAction

