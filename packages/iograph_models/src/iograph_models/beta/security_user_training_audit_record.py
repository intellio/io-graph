from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityUserTrainingAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.userTrainingAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.userTrainingAuditRecord")

