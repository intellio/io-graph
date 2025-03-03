from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventsRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	events: Optional[list[VirtualEvent]] = Field(default=None,alias="events",)
	townhalls: Optional[list[VirtualEventTownhall]] = Field(default=None,alias="townhalls",)
	webinars: Optional[list[VirtualEventWebinar]] = Field(default=None,alias="webinars",)

from .virtual_event import VirtualEvent
from .virtual_event_townhall import VirtualEventTownhall
from .virtual_event_webinar import VirtualEventWebinar

