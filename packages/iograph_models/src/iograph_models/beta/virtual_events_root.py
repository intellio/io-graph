from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class VirtualEventsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEventsRoot"] = Field(alias="@odata.type", default="#microsoft.graph.virtualEventsRoot")
	events: Optional[list[Annotated[Union[VirtualEventTownhall, VirtualEventWebinar],Field(discriminator="odata_type")]]] = Field(alias="events", default=None,)
	townhalls: Optional[list[VirtualEventTownhall]] = Field(alias="townhalls", default=None,)
	webinars: Optional[list[VirtualEventWebinar]] = Field(alias="webinars", default=None,)

from .virtual_event_townhall import VirtualEventTownhall
from .virtual_event_webinar import VirtualEventWebinar
