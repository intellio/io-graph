from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcManagementGroupAssignmentTarget(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allotmentDisplayName: Optional[str] = Field(alias="allotmentDisplayName",default=None,)
	allotmentLicensesCount: Optional[int] = Field(alias="allotmentLicensesCount",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)
	servicePlanId: Optional[str] = Field(alias="servicePlanId",default=None,)


