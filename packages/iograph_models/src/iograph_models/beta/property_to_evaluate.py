from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PropertyToEvaluate(BaseModel):
	propertyName: Optional[str] = Field(alias="propertyName", default=None,)
	propertyValue: Optional[str] = Field(alias="propertyValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

