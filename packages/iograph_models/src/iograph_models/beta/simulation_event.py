from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationEvent(BaseModel):
	count: Optional[int] = Field(alias="count", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


