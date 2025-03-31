from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricQuality(BaseModel):
	criteria: Optional[list[RubricCriterion]] = Field(alias="criteria", default=None,)
	description: Optional[EducationItemBody] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	qualityId: Optional[str] = Field(alias="qualityId", default=None,)
	weight: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .rubric_criterion import RubricCriterion
from .education_item_body import EducationItemBody
from .reference_numeric import ReferenceNumeric
