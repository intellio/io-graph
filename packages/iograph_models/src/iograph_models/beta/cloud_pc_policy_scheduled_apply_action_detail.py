from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcPolicyScheduledApplyActionDetail(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cronScheduleExpression: Optional[str] = Field(alias="cronScheduleExpression",default=None,)
	reservePercentage: Optional[int] = Field(alias="reservePercentage",default=None,)


