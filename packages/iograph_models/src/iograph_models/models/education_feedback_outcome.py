from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedbackOutcome(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	feedback: Optional[EducationFeedback] = Field(default=None,alias="feedback",)
	publishedFeedback: Optional[EducationFeedback] = Field(default=None,alias="publishedFeedback",)

from .identity_set import IdentitySet
from .education_feedback import EducationFeedback
from .education_feedback import EducationFeedback

