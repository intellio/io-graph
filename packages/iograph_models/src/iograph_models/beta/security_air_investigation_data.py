from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAirInvestigationData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.airInvestigationData"] = Field(alias="@odata.type", default="#microsoft.graph.security.airInvestigationData")

