from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCaseInvestigation(BaseModel):
	odata_type: Literal["#microsoft.graph.security.caseInvestigation"] = Field(alias="@odata.type", default="#microsoft.graph.security.caseInvestigation")

