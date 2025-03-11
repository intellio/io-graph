from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageApprovalStage(BaseModel):
	durationBeforeAutomaticDenial: Optional[str] = Field(alias="durationBeforeAutomaticDenial",default=None,)
	durationBeforeEscalation: Optional[str] = Field(alias="durationBeforeEscalation",default=None,)
	escalationApprovers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="escalationApprovers",default=None,)
	fallbackEscalationApprovers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="fallbackEscalationApprovers",default=None,)
	fallbackPrimaryApprovers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="fallbackPrimaryApprovers",default=None,)
	isApproverJustificationRequired: Optional[bool] = Field(alias="isApproverJustificationRequired",default=None,)
	isEscalationEnabled: Optional[bool] = Field(alias="isEscalationEnabled",default=None,)
	primaryApprovers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="primaryApprovers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .subject_set import SubjectSet

