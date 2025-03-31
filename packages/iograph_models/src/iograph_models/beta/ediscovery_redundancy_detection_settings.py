from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EdiscoveryRedundancyDetectionSettings(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	maxWords: Optional[int] = Field(alias="maxWords", default=None,)
	minWords: Optional[int] = Field(alias="minWords", default=None,)
	similarityThreshold: Optional[int] = Field(alias="similarityThreshold", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

