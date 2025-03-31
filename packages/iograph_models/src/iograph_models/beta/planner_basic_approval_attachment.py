from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerBasicApprovalAttachment(BaseModel):
	status: Optional[PlannerApprovalStatus | str] = Field(alias="status", default=None,)
	odata_type: Literal["#microsoft.graph.plannerBasicApprovalAttachment"] = Field(alias="@odata.type", default="#microsoft.graph.plannerBasicApprovalAttachment")
	approvalId: Optional[str] = Field(alias="approvalId", default=None,)

from .planner_approval_status import PlannerApprovalStatus
