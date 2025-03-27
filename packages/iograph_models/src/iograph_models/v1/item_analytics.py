from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemAnalytics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	allTime: Optional[ItemActivityStat] = Field(alias="allTime", default=None,)
	itemActivityStats: Optional[list[ItemActivityStat]] = Field(alias="itemActivityStats", default=None,)
	lastSevenDays: Optional[ItemActivityStat] = Field(alias="lastSevenDays", default=None,)

from .item_activity_stat import ItemActivityStat
from .item_activity_stat import ItemActivityStat
from .item_activity_stat import ItemActivityStat

