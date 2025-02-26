from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationRubricOutcome(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	publishedRubricQualityFeedback: list[RubricQualityFeedbackModel] = Field(alias="publishedRubricQualityFeedback",)
	publishedRubricQualitySelectedLevels: list[RubricQualitySelectedColumnModel] = Field(alias="publishedRubricQualitySelectedLevels",)
	rubricQualityFeedback: list[RubricQualityFeedbackModel] = Field(alias="rubricQualityFeedback",)
	rubricQualitySelectedLevels: list[RubricQualitySelectedColumnModel] = Field(alias="rubricQualitySelectedLevels",)

from .identity_set import IdentitySet
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

