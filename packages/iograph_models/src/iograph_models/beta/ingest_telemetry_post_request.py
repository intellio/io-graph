from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Ingest_telemetryPostRequest(BaseModel):
	telemetry: Optional[list[WorkplaceSensorDeviceTelemetry]] = Field(alias="telemetry",default=None,)

from .workplace_sensor_device_telemetry import WorkplaceSensorDeviceTelemetry

