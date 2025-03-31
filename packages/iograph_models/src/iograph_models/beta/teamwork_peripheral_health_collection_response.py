from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkPeripheralHealthCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TeamworkPeripheralHealth]] = Field(alias="value", default=None,)

from .teamwork_peripheral_health import TeamworkPeripheralHealth
