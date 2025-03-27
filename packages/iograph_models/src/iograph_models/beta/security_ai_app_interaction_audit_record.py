from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAiAppInteractionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aiAppInteractionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.aiAppInteractionAuditRecord")


