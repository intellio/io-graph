from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SingleValueLegacyExtendedPropertyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="value",default=None,)

from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

