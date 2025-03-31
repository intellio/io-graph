from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidForWorkCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidForWorkCompliancePolicy]] = Field(alias="value", default=None,)

from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
