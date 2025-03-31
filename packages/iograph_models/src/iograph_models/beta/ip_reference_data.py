from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IpReferenceData(BaseModel):
	asn: Optional[int] = Field(alias="asn", default=None,)
	city: Optional[str] = Field(alias="city", default=None,)
	countryOrRegionCode: Optional[str] = Field(alias="countryOrRegionCode", default=None,)
	organization: Optional[str] = Field(alias="organization", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	vendor: Optional[str] = Field(alias="vendor", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

