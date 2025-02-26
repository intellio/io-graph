from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageApprovalStage(BaseModel):
	durationBeforeAutomaticDenial: Optional[str] = Field(default=None,alias="durationBeforeAutomaticDenial",)
	durationBeforeEscalation: Optional[str] = Field(default=None,alias="durationBeforeEscalation",)
	escalationApprovers: list[SubjectSet] = Field(alias="escalationApprovers",)
	fallbackEscalationApprovers: list[SubjectSet] = Field(alias="fallbackEscalationApprovers",)
	fallbackPrimaryApprovers: list[SubjectSet] = Field(alias="fallbackPrimaryApprovers",)
	isApproverJustificationRequired: Optional[bool] = Field(default=None,alias="isApproverJustificationRequired",)
	isEscalationEnabled: Optional[bool] = Field(default=None,alias="isEscalationEnabled",)
	primaryApprovers: list[SubjectSet] = Field(alias="primaryApprovers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .subject_set import SubjectSet

