from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessFilter(BaseModel):
	mode: Optional[FilterMode | str] = Field(alias="mode", default=None,)
	rule: Optional[str] = Field(alias="rule", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .filter_mode import FilterMode
