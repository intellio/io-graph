from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcFrontLineServicePlan(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcFrontLineServicePlan"] = Field(alias="@odata.type",)
	allotmentLicensesCount: Optional[int] = Field(alias="allotmentLicensesCount", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	totalCount: Optional[int] = Field(alias="totalCount", default=None,)
	usedCount: Optional[int] = Field(alias="usedCount", default=None,)

