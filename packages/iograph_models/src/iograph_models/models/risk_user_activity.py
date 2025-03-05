from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RiskUserActivity(BaseModel):
	detail: Optional[RiskDetail] = Field(default=None,alias="detail",)
	riskEventTypes: Optional[list[str]] = Field(default=None,alias="riskEventTypes",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .risk_detail import RiskDetail

