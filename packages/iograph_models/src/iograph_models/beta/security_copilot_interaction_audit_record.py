from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCopilotInteractionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.copilotInteractionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.copilotInteractionAuditRecord")


