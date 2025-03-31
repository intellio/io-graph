from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityVivaLearningAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vivaLearningAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vivaLearningAuditRecord")

