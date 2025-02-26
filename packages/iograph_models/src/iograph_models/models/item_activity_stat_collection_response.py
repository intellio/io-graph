from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemActivityStatCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ItemActivityStat] = Field(alias="value",)

from .item_activity_stat import ItemActivityStat

