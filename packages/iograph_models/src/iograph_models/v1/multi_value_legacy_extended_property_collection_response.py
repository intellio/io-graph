from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiValueLegacyExtendedPropertyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="value",default=None,)

from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty

