from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationAutomation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[EmailIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[EmailIdentity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	lastRunDateTime: Optional[datetime] = Field(default=None,alias="lastRunDateTime",)
	nextRunDateTime: Optional[datetime] = Field(default=None,alias="nextRunDateTime",)
	status: Optional[SimulationAutomationStatus] = Field(default=None,alias="status",)
	runs: Optional[list[SimulationAutomationRun]] = Field(default=None,alias="runs",)

from .email_identity import EmailIdentity
from .email_identity import EmailIdentity
from .simulation_automation_status import SimulationAutomationStatus
from .simulation_automation_run import SimulationAutomationRun

