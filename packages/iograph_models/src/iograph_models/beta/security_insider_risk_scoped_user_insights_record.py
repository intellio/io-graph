from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityInsiderRiskScopedUserInsightsRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.insiderRiskScopedUserInsightsRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.insiderRiskScopedUserInsightsRecord")


