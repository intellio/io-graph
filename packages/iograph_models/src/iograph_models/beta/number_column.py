from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NumberColumn(BaseModel):
	decimalPlaces: Optional[str] = Field(alias="decimalPlaces", default=None,)
	displayAs: Optional[str] = Field(alias="displayAs", default=None,)
	maximum: float | str | ReferenceNumeric
	minimum: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

