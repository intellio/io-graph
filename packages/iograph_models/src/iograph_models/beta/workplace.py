from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Workplace(BaseModel):
	sensorDevices: Optional[list[WorkplaceSensorDevice]] = Field(alias="sensorDevices",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .workplace_sensor_device import WorkplaceSensorDevice

