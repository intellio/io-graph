from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PhysicalAddress(BaseModel):
	city: Optional[str] = Field(alias="city", default=None,)
	countryOrRegion: Optional[str] = Field(alias="countryOrRegion", default=None,)
	postalCode: Optional[str] = Field(alias="postalCode", default=None,)
	postOfficeBox: Optional[str] = Field(alias="postOfficeBox", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	street: Optional[str] = Field(alias="street", default=None,)
	type: Optional[PhysicalAddressType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .physical_address_type import PhysicalAddressType
