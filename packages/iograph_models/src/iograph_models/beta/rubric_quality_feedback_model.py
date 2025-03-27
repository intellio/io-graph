from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricQualityFeedbackModel(BaseModel):
	feedback: Optional[EducationItemBody] = Field(alias="feedback", default=None,)
	qualityId: Optional[str] = Field(alias="qualityId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .education_item_body import EducationItemBody

