from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SimulationAutomation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.simulationAutomation"] = Field(alias="@odata.type",)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lastRunDateTime: Optional[datetime] = Field(alias="lastRunDateTime", default=None,)
	nextRunDateTime: Optional[datetime] = Field(alias="nextRunDateTime", default=None,)
	status: Optional[SimulationAutomationStatus | str] = Field(alias="status", default=None,)
	runs: Optional[list[SimulationAutomationRun]] = Field(alias="runs", default=None,)

from .email_identity import EmailIdentity
from .simulation_automation_status import SimulationAutomationStatus
from .simulation_automation_run import SimulationAutomationRun
