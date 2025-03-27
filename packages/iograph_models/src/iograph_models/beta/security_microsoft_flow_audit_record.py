from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoftFlowAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftFlowAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftFlowAuditRecord")


