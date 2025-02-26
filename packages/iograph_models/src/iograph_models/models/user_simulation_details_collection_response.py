from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserSimulationDetailsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserSimulationDetails] = Field(alias="value",)

from .user_simulation_details import UserSimulationDetails

