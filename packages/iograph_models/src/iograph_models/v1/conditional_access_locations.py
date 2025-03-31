from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessLocations(BaseModel):
	excludeLocations: Optional[list[str]] = Field(alias="excludeLocations", default=None,)
	includeLocations: Optional[list[str]] = Field(alias="includeLocations", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

