from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10CompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10CompliancePolicy]] = Field(alias="value", default=None,)

from .windows10_compliance_policy import Windows10CompliancePolicy
