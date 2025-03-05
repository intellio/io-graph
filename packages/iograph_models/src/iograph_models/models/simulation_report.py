from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationReport(BaseModel):
	overview: Optional[SimulationReportOverview] = Field(default=None,alias="overview",)
	simulationUsers: Optional[list[UserSimulationDetails]] = Field(default=None,alias="simulationUsers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .simulation_report_overview import SimulationReportOverview
from .user_simulation_details import UserSimulationDetails

