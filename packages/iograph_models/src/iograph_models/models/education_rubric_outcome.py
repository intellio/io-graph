from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationRubricOutcome(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	publishedRubricQualityFeedback: Optional[list[RubricQualityFeedbackModel]] = Field(default=None,alias="publishedRubricQualityFeedback",)
	publishedRubricQualitySelectedLevels: Optional[list[RubricQualitySelectedColumnModel]] = Field(default=None,alias="publishedRubricQualitySelectedLevels",)
	rubricQualityFeedback: Optional[list[RubricQualityFeedbackModel]] = Field(default=None,alias="rubricQualityFeedback",)
	rubricQualitySelectedLevels: Optional[list[RubricQualitySelectedColumnModel]] = Field(default=None,alias="rubricQualitySelectedLevels",)

from .identity_set import IdentitySet
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

