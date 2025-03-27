from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OidcAddressInboundClaims(BaseModel):
	country: Optional[str] = Field(alias="country", default=None,)
	locality: Optional[str] = Field(alias="locality", default=None,)
	postal_code: Optional[str] = Field(alias="postal_code", default=None,)
	region: Optional[str] = Field(alias="region", default=None,)
	street_address: Optional[str] = Field(alias="street_address", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


