from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PhoneOptions(BaseModel):
	defaultRegions: Optional[list[int]] = Field(alias="defaultRegions", default=None,)
	excludeRegions: Optional[list[int]] = Field(alias="excludeRegions", default=None,)
	includeAdditionalRegions: Optional[list[int]] = Field(alias="includeAdditionalRegions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

