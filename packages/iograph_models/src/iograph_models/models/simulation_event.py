from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SimulationEvent(BaseModel):
	count: Optional[int] = Field(default=None,alias="count",)
	eventName: Optional[str] = Field(default=None,alias="eventName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


