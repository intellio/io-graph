from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StaffAvailabilityItem(BaseModel):
	availabilityItems: Optional[list[AvailabilityItem]] = Field(default=None,alias="availabilityItems",)
	staffId: Optional[str] = Field(default=None,alias="staffId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .availability_item import AvailabilityItem

