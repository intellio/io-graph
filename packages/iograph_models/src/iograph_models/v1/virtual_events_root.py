from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventsRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	events: SerializeAsAny[Optional[list[VirtualEvent]]] = Field(alias="events",default=None,)
	townhalls: Optional[list[VirtualEventTownhall]] = Field(alias="townhalls",default=None,)
	webinars: Optional[list[VirtualEventWebinar]] = Field(alias="webinars",default=None,)

from .virtual_event import VirtualEvent
from .virtual_event_townhall import VirtualEventTownhall
from .virtual_event_webinar import VirtualEventWebinar

