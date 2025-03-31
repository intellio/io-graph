from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityScoreEvidence(BaseModel):
	odata_type: Literal["#microsoft.graph.security.scoreEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.scoreEvidence")

