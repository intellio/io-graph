from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkplaceSensor(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	placeId: Optional[str] = Field(alias="placeId", default=None,)
	sensorId: Optional[str] = Field(alias="sensorId", default=None,)
	sensorType: Optional[WorkplaceSensorType | str] = Field(alias="sensorType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .workplace_sensor_type import WorkplaceSensorType
