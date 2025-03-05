from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricQualitySelectedColumnModelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[RubricQualitySelectedColumnModel]] = Field(default=None,alias="value",)

from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

