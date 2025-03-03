from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SingleValueLegacyExtendedPropertyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="value",)

from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

