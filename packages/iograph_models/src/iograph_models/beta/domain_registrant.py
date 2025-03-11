from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DomainRegistrant(BaseModel):
	countryOrRegionCode: Optional[str] = Field(alias="countryOrRegionCode",default=None,)
	organization: Optional[str] = Field(alias="organization",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)
	vendor: Optional[str] = Field(alias="vendor",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


