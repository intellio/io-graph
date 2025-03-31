from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SimulationAutomationRun(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.simulationAutomationRun"] = Field(alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	simulationId: Optional[str] = Field(alias="simulationId", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[SimulationAutomationRunStatus | str] = Field(alias="status", default=None,)

from .simulation_automation_run_status import SimulationAutomationRunStatus
