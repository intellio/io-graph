from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedApprovalStage(BaseModel):
	approvalStageTimeOutInDays: Optional[int] = Field(default=None,alias="approvalStageTimeOutInDays",)
	escalationApprovers: Optional[list[SubjectSet]] = Field(default=None,alias="escalationApprovers",)
	escalationTimeInMinutes: Optional[int] = Field(default=None,alias="escalationTimeInMinutes",)
	isApproverJustificationRequired: Optional[bool] = Field(default=None,alias="isApproverJustificationRequired",)
	isEscalationEnabled: Optional[bool] = Field(default=None,alias="isEscalationEnabled",)
	primaryApprovers: Optional[list[SubjectSet]] = Field(default=None,alias="primaryApprovers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .subject_set import SubjectSet
from .subject_set import SubjectSet

