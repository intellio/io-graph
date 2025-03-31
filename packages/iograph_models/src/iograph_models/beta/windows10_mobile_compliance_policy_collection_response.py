from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10MobileCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10MobileCompliancePolicy]] = Field(alias="value", default=None,)

from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
