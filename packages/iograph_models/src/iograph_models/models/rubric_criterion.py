from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricCriterion(BaseModel):
	description: Optional[EducationItemBody] = Field(default=None,alias="description",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .education_item_body import EducationItemBody

