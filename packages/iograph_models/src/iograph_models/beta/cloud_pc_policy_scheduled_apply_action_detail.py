from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcPolicyScheduledApplyActionDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcPolicyScheduledApplyActionDetail"] = Field(alias="@odata.type",)
	cronScheduleExpression: Optional[str] = Field(alias="cronScheduleExpression", default=None,)
	reservePercentage: Optional[int] = Field(alias="reservePercentage", default=None,)

