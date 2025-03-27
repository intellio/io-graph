from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityThreatIntelligenceMailData(BaseModel):
	odata_type: Literal["#microsoft.graph.security.threatIntelligenceMailData"] = Field(alias="@odata.type", default="#microsoft.graph.security.threatIntelligenceMailData")


