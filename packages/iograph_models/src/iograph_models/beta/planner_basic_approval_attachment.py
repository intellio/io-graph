from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBasicApprovalAttachment(BaseModel):
	status: Optional[PlannerApprovalStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	approvalId: Optional[str] = Field(alias="approvalId",default=None,)

from .planner_approval_status import PlannerApprovalStatus

