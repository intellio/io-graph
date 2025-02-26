from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeOffRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TimeOffRequest] = Field(alias="value",)

from .time_off_request import TimeOffRequest

