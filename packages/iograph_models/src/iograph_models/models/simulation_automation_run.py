from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationAutomationRun(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	simulationId: Optional[str] = Field(alias="simulationId",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	status: Optional[str | SimulationAutomationRunStatus] = Field(alias="status",default=None,)

from .simulation_automation_run_status import SimulationAutomationRunStatus

