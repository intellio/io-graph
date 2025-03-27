from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkHardwareConfiguration(BaseModel):
	processorModel: Optional[str] = Field(alias="processorModel", default=None,)
	compute: Optional[TeamworkPeripheral] = Field(alias="compute", default=None,)
	hdmiIngest: Optional[TeamworkPeripheral] = Field(alias="hdmiIngest", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral

