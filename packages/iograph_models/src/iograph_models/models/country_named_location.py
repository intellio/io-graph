from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CountryNamedLocation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	countriesAndRegions: list[str] = Field(alias="countriesAndRegions",)
	countryLookupMethod: Optional[CountryLookupMethodType] = Field(default=None,alias="countryLookupMethod",)
	includeUnknownCountriesAndRegions: Optional[bool] = Field(default=None,alias="includeUnknownCountriesAndRegions",)

from .country_lookup_method_type import CountryLookupMethodType

