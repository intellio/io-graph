from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricQualitySelectedColumnModelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[RubricQualitySelectedColumnModel]] = Field(alias="value",default=None,)

from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel

