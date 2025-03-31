from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ItemInsights(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemInsights"] = Field(alias="@odata.type",)
	shared: Optional[list[SharedInsight]] = Field(alias="shared", default=None,)
	trending: Optional[list[Trending]] = Field(alias="trending", default=None,)
	used: Optional[list[UsedInsight]] = Field(alias="used", default=None,)

from .shared_insight import SharedInsight
from .trending import Trending
from .used_insight import UsedInsight
