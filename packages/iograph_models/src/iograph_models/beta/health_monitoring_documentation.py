from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class HealthMonitoringDocumentation(BaseModel):
	odata_type: Literal["#microsoft.graph.healthMonitoring.documentation"] = Field(alias="@odata.type",)

