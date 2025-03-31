from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WorkplaceSensorDeviceTelemetry(BaseModel):
	boolValue: Optional[bool] = Field(alias="boolValue", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	eventValue: Optional[WorkplaceSensorEventValue] = Field(alias="eventValue", default=None,)
	intValue: Optional[int] = Field(alias="intValue", default=None,)
	locationHint: Optional[str] = Field(alias="locationHint", default=None,)
	sensorId: Optional[str] = Field(alias="sensorId", default=None,)
	sensorType: Optional[WorkplaceSensorType | str] = Field(alias="sensorType", default=None,)
	timestamp: Optional[datetime] = Field(alias="timestamp", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .workplace_sensor_event_value import WorkplaceSensorEventValue
from .workplace_sensor_type import WorkplaceSensorType
