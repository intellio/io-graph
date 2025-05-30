from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AverageComparativeScore(BaseModel):
	averageScore: float | str | ReferenceNumeric
	basis: Optional[str] = Field(alias="basis", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
