from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityGeoLocation(BaseModel):
	city: Optional[str] = Field(default=None,alias="city",)
	countryName: Optional[str] = Field(default=None,alias="countryName",)
	latitude: Optional[float] | Optional[str] | ReferenceNumeric
	longitude: Optional[float] | Optional[str] | ReferenceNumeric
	state: Optional[str] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

