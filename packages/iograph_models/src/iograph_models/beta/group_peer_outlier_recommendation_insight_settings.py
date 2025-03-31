from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class GroupPeerOutlierRecommendationInsightSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.groupPeerOutlierRecommendationInsightSettings"] = Field(alias="@odata.type", default="#microsoft.graph.groupPeerOutlierRecommendationInsightSettings")

