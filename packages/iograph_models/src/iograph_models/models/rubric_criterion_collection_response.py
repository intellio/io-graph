from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricCriterionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RubricCriterion] = Field(alias="value",)

from .rubric_criterion import RubricCriterion

