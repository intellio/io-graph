from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationReport(BaseModel):
	overview: Optional[SimulationReportOverview] = Field(alias="overview",default=None,)
	simulationUsers: Optional[list[UserSimulationDetails]] = Field(alias="simulationUsers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .simulation_report_overview import SimulationReportOverview
from .user_simulation_details import UserSimulationDetails

