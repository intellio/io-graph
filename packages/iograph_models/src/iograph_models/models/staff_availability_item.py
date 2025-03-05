from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StaffAvailabilityItem(BaseModel):
	availabilityItems: Optional[list[AvailabilityItem]] = Field(alias="availabilityItems",default=None,)
	staffId: Optional[str] = Field(alias="staffId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .availability_item import AvailabilityItem

