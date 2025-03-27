from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPowerAppsAuditAppRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerAppsAuditAppRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerAppsAuditAppRecord")


