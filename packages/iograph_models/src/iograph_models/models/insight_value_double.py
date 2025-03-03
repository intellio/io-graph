from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InsightValueDouble(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

