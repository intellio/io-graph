from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RiskyUserHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[RiskyUserHistoryItem]] = Field(default=None,alias="value",)

from .risky_user_history_item import RiskyUserHistoryItem

