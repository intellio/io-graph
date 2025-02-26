from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ActivityHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ActivityHistoryItem] = Field(alias="value",)

from .activity_history_item import ActivityHistoryItem

