from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemInsights(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	shared: list[SharedInsight] = Field(alias="shared",)
	trending: list[Trending] = Field(alias="trending",)
	used: list[UsedInsight] = Field(alias="used",)

from .shared_insight import SharedInsight
from .trending import Trending
from .used_insight import UsedInsight

