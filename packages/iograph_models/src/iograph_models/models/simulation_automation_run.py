from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationAutomationRun(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	simulationId: Optional[str] = Field(default=None,alias="simulationId",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	status: Optional[SimulationAutomationRunStatus] = Field(default=None,alias="status",)

from .simulation_automation_run_status import SimulationAutomationRunStatus

