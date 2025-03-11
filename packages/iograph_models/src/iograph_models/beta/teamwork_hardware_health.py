from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkHardwareHealth(BaseModel):
	computeHealth: Optional[TeamworkPeripheralHealth] = Field(alias="computeHealth",default=None,)
	hdmiIngestHealth: Optional[TeamworkPeripheralHealth] = Field(alias="hdmiIngestHealth",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_peripheral_health import TeamworkPeripheralHealth
from .teamwork_peripheral_health import TeamworkPeripheralHealth

