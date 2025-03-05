from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedbackResourceOutcome(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	feedbackResource: SerializeAsAny[Optional[EducationResource]] = Field(default=None,alias="feedbackResource",)
	resourceStatus: Optional[EducationFeedbackResourceOutcomeStatus] = Field(default=None,alias="resourceStatus",)

from .identity_set import IdentitySet
from .education_resource import EducationResource
from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus

