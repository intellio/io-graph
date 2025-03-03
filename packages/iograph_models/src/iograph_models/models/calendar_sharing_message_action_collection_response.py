from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CalendarSharingMessageActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CalendarSharingMessageAction]] = Field(default=None,alias="value",)

from .calendar_sharing_message_action import CalendarSharingMessageAction

