from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ItemAnalytics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemAnalytics"] = Field(alias="@odata.type",)
	allTime: Optional[ItemActivityStat] = Field(alias="allTime", default=None,)
	itemActivityStats: Optional[list[ItemActivityStat]] = Field(alias="itemActivityStats", default=None,)
	lastSevenDays: Optional[ItemActivityStat] = Field(alias="lastSevenDays", default=None,)

from .item_activity_stat import ItemActivityStat
