from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GeoCoordinates(BaseModel):
	altitude: Optional[float] | Optional[str] | ReferenceNumeric
	latitude: Optional[float] | Optional[str] | ReferenceNumeric
	longitude: Optional[float] | Optional[str] | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

