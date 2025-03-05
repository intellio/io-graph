from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CountryNamedLocation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	countriesAndRegions: Optional[list[str]] = Field(alias="countriesAndRegions",default=None,)
	countryLookupMethod: Optional[str | CountryLookupMethodType] = Field(alias="countryLookupMethod",default=None,)
	includeUnknownCountriesAndRegions: Optional[bool] = Field(alias="includeUnknownCountriesAndRegions",default=None,)

from .country_lookup_method_type import CountryLookupMethodType

