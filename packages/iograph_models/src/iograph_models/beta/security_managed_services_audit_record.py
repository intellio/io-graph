from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityManagedServicesAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.managedServicesAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.managedServicesAuditRecord")

