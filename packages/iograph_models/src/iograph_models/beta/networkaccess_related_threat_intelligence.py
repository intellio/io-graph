from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessRelatedThreatIntelligence(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedThreatIntelligence"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedThreatIntelligence")
	threatCount: Optional[int] = Field(alias="threatCount", default=None,)

