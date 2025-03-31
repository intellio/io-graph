from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityThreatIntelligenceUrlClickData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.threatIntelligenceUrlClickData"] = Field(alias="@odata.type", default="#microsoft.graph.security.threatIntelligenceUrlClickData")

