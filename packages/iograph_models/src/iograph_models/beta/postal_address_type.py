from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PostalAddressType(BaseModel):
	city: Optional[str] = Field(alias="city", default=None,)
	countryLetterCode: Optional[str] = Field(alias="countryLetterCode", default=None,)
	postalCode: Optional[str] = Field(alias="postalCode", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	street: Optional[str] = Field(alias="street", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

