from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10CompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Windows10CompliancePolicy] = Field(alias="value",)

from .windows10_compliance_policy import Windows10CompliancePolicy

