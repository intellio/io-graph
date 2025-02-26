from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_staff_availabilityPostResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[StaffAvailabilityItem] = Field(alias="value",)

from .staff_availability_item import StaffAvailabilityItem

