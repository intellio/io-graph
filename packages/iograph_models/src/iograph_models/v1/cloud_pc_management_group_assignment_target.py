from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcManagementGroupAssignmentTarget(BaseModel):
	odata_type: Literal["#microsoft.graph.cloudPcManagementGroupAssignmentTarget"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcManagementGroupAssignmentTarget")
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	servicePlanId: Optional[str] = Field(alias="servicePlanId", default=None,)

