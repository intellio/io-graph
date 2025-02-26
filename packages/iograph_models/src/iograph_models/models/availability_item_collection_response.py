from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AvailabilityItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AvailabilityItem] = Field(alias="value",)

from .availability_item import AvailabilityItem

