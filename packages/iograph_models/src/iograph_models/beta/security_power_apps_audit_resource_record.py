from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPowerAppsAuditResourceRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerAppsAuditResourceRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerAppsAuditResourceRecord")

