from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcFrontLineServicePlan(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allotmentLicensesCount: Optional[int] = Field(alias="allotmentLicensesCount",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	totalCount: Optional[int] = Field(alias="totalCount",default=None,)
	usedCount: Optional[int] = Field(alias="usedCount",default=None,)


