from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarSharingMessageActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CalendarSharingMessageAction]] = Field(alias="value", default=None,)

from .calendar_sharing_message_action import CalendarSharingMessageAction

