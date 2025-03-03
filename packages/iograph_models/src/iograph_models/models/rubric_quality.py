from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricQuality(BaseModel):
	criteria: Optional[list[RubricCriterion]] = Field(default=None,alias="criteria",)
	description: Optional[EducationItemBody] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	qualityId: Optional[str] = Field(default=None,alias="qualityId",)
	weight: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rubric_criterion import RubricCriterion
from .education_item_body import EducationItemBody
from .reference_numeric import ReferenceNumeric

