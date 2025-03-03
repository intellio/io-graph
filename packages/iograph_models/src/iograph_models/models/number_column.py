from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NumberColumn(BaseModel):
	decimalPlaces: Optional[str] = Field(default=None,alias="decimalPlaces",)
	displayAs: Optional[str] = Field(default=None,alias="displayAs",)
	maximum: float | str | ReferenceNumeric
	minimum: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

