from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemAnalytics(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allTime: Optional[ItemActivityStat] = Field(default=None,alias="allTime",)
	itemActivityStats: Optional[list[ItemActivityStat]] = Field(default=None,alias="itemActivityStats",)
	lastSevenDays: Optional[ItemActivityStat] = Field(default=None,alias="lastSevenDays",)

from .item_activity_stat import ItemActivityStat
from .item_activity_stat import ItemActivityStat
from .item_activity_stat import ItemActivityStat

