from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeCardCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TimeCard] = Field(alias="value",)

from .time_card import TimeCard

