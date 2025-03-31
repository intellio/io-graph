from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityGeoLocation(BaseModel):
	city: Optional[str] = Field(alias="city", default=None,)
	countryName: Optional[str] = Field(alias="countryName", default=None,)
	latitude: float | str | ReferenceNumeric
	longitude: float | str | ReferenceNumeric
	state: Optional[str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
