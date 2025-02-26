from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SimulationEventsContent(BaseModel):
	compromisedRate: Optional[float] | Optional[str] | ReferenceNumeric
	events: list[SimulationEvent] = Field(alias="events",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .simulation_event import SimulationEvent

