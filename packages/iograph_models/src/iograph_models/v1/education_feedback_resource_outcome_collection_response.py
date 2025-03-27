from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedbackResourceOutcomeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EducationFeedbackResourceOutcome]] = Field(alias="value", default=None,)

from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome

