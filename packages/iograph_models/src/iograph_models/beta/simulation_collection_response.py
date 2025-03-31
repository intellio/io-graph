from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SimulationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Simulation]] = Field(alias="value", default=None,)

from .simulation import Simulation
