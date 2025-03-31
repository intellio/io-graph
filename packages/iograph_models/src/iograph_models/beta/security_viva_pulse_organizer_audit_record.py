from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityVivaPulseOrganizerAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vivaPulseOrganizerAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vivaPulseOrganizerAuditRecord")

