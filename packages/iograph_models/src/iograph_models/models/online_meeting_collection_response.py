from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnlineMeetingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OnlineMeeting] = Field(alias="value",)

from .online_meeting import OnlineMeeting

