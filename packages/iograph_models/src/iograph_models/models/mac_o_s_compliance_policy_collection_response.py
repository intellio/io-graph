from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MacOSCompliancePolicy]] = Field(default=None,alias="value",)

from .mac_o_s_compliance_policy import MacOSCompliancePolicy

