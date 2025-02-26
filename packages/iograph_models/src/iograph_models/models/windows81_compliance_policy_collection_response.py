from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows81CompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Windows81CompliancePolicy] = Field(alias="value",)

from .windows81_compliance_policy import Windows81CompliancePolicy

