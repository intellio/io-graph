from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SwapShiftsChangeRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SwapShiftsChangeRequest]] = Field(alias="value",default=None,)

from .swap_shifts_change_request import SwapShiftsChangeRequest

