from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AverageComparativeScore(BaseModel):
	averageScore: Optional[float] | Optional[str] | ReferenceNumeric
	basis: Optional[str] = Field(default=None,alias="basis",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric

