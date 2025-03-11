from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricQualityFeedbackModelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[RubricQualityFeedbackModel]] = Field(alias="value",default=None,)

from .rubric_quality_feedback_model import RubricQualityFeedbackModel

