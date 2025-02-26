from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessLocations(BaseModel):
	excludeLocations: list[str] = Field(alias="excludeLocations",)
	includeLocations: list[str] = Field(alias="includeLocations",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


