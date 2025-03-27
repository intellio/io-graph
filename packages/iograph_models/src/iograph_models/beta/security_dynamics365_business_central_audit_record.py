from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDynamics365BusinessCentralAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dynamics365BusinessCentralAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dynamics365BusinessCentralAuditRecord")


