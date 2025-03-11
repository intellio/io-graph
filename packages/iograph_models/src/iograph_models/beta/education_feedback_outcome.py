from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedbackOutcome(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	feedback: Optional[EducationFeedback] = Field(alias="feedback",default=None,)
	publishedFeedback: Optional[EducationFeedback] = Field(alias="publishedFeedback",default=None,)

from .identity_set import IdentitySet
from .education_feedback import EducationFeedback
from .education_feedback import EducationFeedback

