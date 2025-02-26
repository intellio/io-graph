from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LocationConstraintItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[LocationConstraintItem] = Field(alias="value",)

from .location_constraint_item import LocationConstraintItem

