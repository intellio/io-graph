from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SwapShiftsChangeRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SwapShiftsChangeRequest]] = Field(default=None,alias="value",)

from .swap_shifts_change_request import SwapShiftsChangeRequest

