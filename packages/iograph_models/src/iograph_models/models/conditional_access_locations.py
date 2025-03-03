from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessLocations(BaseModel):
	excludeLocations: Optional[list[str]] = Field(default=None,alias="excludeLocations",)
	includeLocations: Optional[list[str]] = Field(default=None,alias="includeLocations",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


