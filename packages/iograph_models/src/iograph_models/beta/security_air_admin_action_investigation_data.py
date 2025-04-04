from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAirAdminActionInvestigationData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.airAdminActionInvestigationData"] = Field(alias="@odata.type", default="#microsoft.graph.security.airAdminActionInvestigationData")

