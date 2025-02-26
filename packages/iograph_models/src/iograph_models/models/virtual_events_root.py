from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventsRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	events: list[VirtualEvent] = Field(alias="events",)
	townhalls: list[VirtualEventTownhall] = Field(alias="townhalls",)
	webinars: list[VirtualEventWebinar] = Field(alias="webinars",)

from .virtual_event import VirtualEvent
from .virtual_event_townhall import VirtualEventTownhall
from .virtual_event_webinar import VirtualEventWebinar

