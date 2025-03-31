from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftDefenderExpertsBaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftDefenderExpertsBaseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftDefenderExpertsBaseAuditRecord")

