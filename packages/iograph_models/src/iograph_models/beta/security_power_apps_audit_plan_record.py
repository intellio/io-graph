from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPowerAppsAuditPlanRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerAppsAuditPlanRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerAppsAuditPlanRecord")

