from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPlannerTenantSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.plannerTenantSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.plannerTenantSettingsAuditRecord")

