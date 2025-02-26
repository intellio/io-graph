from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessFilter(BaseModel):
	mode: Optional[FilterMode] = Field(default=None,alias="mode",)
	rule: Optional[str] = Field(default=None,alias="rule",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .filter_mode import FilterMode

