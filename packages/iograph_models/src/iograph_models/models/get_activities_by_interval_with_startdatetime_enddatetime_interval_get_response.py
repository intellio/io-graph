from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_activities_by_interval_with_startdatetime_enddatetime_intervalGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ItemActivityStat]] = Field(default=None,alias="value",)

from .item_activity_stat import ItemActivityStat

