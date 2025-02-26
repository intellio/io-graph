from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationFeedbackResourceOutcomeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EducationFeedbackResourceOutcome] = Field(alias="value",)

from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome

