from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMS365DSuppressionRuleAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mS365DSuppressionRuleAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mS365DSuppressionRuleAuditRecord")

