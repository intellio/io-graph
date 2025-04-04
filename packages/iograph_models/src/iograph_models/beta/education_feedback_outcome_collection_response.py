from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationFeedbackOutcomeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EducationFeedbackOutcome]] = Field(alias="value", default=None,)

from .education_feedback_outcome import EducationFeedbackOutcome
