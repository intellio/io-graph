from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAirManualInvestigationData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.airManualInvestigationData"] = Field(alias="@odata.type", default="#microsoft.graph.security.airManualInvestigationData")

