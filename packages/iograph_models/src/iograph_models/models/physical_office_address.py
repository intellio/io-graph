from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PhysicalOfficeAddress(BaseModel):
	city: Optional[str] = Field(default=None,alias="city",)
	countryOrRegion: Optional[str] = Field(default=None,alias="countryOrRegion",)
	officeLocation: Optional[str] = Field(default=None,alias="officeLocation",)
	postalCode: Optional[str] = Field(default=None,alias="postalCode",)
	state: Optional[str] = Field(default=None,alias="state",)
	street: Optional[str] = Field(default=None,alias="street",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


