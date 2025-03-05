from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricQualityFeedbackModel(BaseModel):
	feedback: Optional[EducationItemBody] = Field(default=None,alias="feedback",)
	qualityId: Optional[str] = Field(default=None,alias="qualityId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .education_item_body import EducationItemBody

