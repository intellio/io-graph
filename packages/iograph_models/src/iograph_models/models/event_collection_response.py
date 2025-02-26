from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Event] = Field(alias="value",)

from .event import Event

