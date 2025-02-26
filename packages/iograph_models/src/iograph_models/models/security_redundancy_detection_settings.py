from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityRedundancyDetectionSettings(BaseModel):
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	maxWords: Optional[int] = Field(default=None,alias="maxWords",)
	minWords: Optional[int] = Field(default=None,alias="minWords",)
	similarityThreshold: Optional[int] = Field(default=None,alias="similarityThreshold",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


