from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationRubricOutcome(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publishedRubricQualityFeedback: Optional[list[RubricQualityFeedbackModel]] = Field(alias="publishedRubricQualityFeedback",default=None,)
	publishedRubricQualitySelectedLevels: Optional[list[RubricQualitySelectedColumnModel]] = Field(alias="publishedRubricQualitySelectedLevels",default=None,)
	rubricQualityFeedback: Optional[list[RubricQualityFeedbackModel]] = Field(alias="rubricQualityFeedback",default=None,)
	rubricQualitySelectedLevels: Optional[list[RubricQualitySelectedColumnModel]] = Field(alias="rubricQualitySelectedLevels",default=None,)

from .identity_set import IdentitySet
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

