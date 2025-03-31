from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlertDetection(BaseModel):
	detectionType: Optional[str] = Field(alias="detectionType", default=None,)
	method: Optional[str] = Field(alias="method", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

