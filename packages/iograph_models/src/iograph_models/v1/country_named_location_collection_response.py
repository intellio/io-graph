from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CountryNamedLocationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CountryNamedLocation]] = Field(alias="value",default=None,)

from .country_named_location import CountryNamedLocation

