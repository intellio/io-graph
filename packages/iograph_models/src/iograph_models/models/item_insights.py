from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemInsights(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	shared: Optional[list[SharedInsight]] = Field(default=None,alias="shared",)
	trending: Optional[list[Trending]] = Field(default=None,alias="trending",)
	used: Optional[list[UsedInsight]] = Field(default=None,alias="used",)

from .shared_insight import SharedInsight
from .trending import Trending
from .used_insight import UsedInsight

