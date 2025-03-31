from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityThreatIntelligenceAtpContentData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.threatIntelligenceAtpContentData"] = Field(alias="@odata.type", default="#microsoft.graph.security.threatIntelligenceAtpContentData")

