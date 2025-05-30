from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class HealthMonitoringSignals(BaseModel):
	odata_type: Literal["#microsoft.graph.healthMonitoring.signals"] = Field(alias="@odata.type", default="#microsoft.graph.healthMonitoring.signals")

