from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedbackResourceOutcome(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	feedbackResource: SerializeAsAny[Optional[EducationResource]] = Field(alias="feedbackResource",default=None,)
	resourceStatus: Optional[EducationFeedbackResourceOutcomeStatus | str] = Field(alias="resourceStatus",default=None,)

from .identity_set import IdentitySet
from .education_resource import EducationResource
from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus

