from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EventMessageRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EventMessageRequest] = Field(alias="value",)

from .event_message_request import EventMessageRequest

