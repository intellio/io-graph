from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageApprovalStage(BaseModel):
	durationBeforeAutomaticDenial: Optional[str] = Field(default=None,alias="durationBeforeAutomaticDenial",)
	durationBeforeEscalation: Optional[str] = Field(default=None,alias="durationBeforeEscalation",)
	escalationApprovers: Optional[list[SubjectSet]] = Field(default=None,alias="escalationApprovers",)
	fallbackEscalationApprovers: Optional[list[SubjectSet]] = Field(default=None,alias="fallbackEscalationApprovers",)
	fallbackPrimaryApprovers: Optional[list[SubjectSet]] = Field(default=None,alias="fallbackPrimaryApprovers",)
	isApproverJustificationRequired: Optional[bool] = Field(default=None,alias="isApproverJustificationRequired",)
	isEscalationEnabled: Optional[bool] = Field(default=None,alias="isEscalationEnabled",)
	primaryApprovers: Optional[list[SubjectSet]] = Field(default=None,alias="primaryApprovers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .subject_set import SubjectSet

