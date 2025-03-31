from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SimulationEventsContent(BaseModel):
	compromisedRate: float | str | ReferenceNumeric
	events: Optional[list[SimulationEvent]] = Field(alias="events", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
from .simulation_event import SimulationEvent
