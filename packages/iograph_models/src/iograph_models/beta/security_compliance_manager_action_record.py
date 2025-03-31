from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceManagerActionRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceManagerActionRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceManagerActionRecord")

