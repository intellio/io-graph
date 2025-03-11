from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricCriterion(BaseModel):
	description: Optional[EducationItemBody] = Field(alias="description",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .education_item_body import EducationItemBody

