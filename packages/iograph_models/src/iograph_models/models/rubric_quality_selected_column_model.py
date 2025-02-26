from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricQualitySelectedColumnModel(BaseModel):
	columnId: Optional[str] = Field(default=None,alias="columnId",)
	qualityId: Optional[str] = Field(default=None,alias="qualityId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


