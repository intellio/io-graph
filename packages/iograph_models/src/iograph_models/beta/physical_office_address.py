from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PhysicalOfficeAddress(BaseModel):
	city: Optional[str] = Field(alias="city", default=None,)
	countryOrRegion: Optional[str] = Field(alias="countryOrRegion", default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation", default=None,)
	postalCode: Optional[str] = Field(alias="postalCode", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	street: Optional[str] = Field(alias="street", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


