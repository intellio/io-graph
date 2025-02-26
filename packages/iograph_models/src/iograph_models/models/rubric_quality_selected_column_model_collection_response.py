from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricQualitySelectedColumnModelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RubricQualitySelectedColumnModel] = Field(alias="value",)

from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

