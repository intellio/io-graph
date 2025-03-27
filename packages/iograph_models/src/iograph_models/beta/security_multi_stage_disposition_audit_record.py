from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMultiStageDispositionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.multiStageDispositionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.multiStageDispositionAuditRecord")


