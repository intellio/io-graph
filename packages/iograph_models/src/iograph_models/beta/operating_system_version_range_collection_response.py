from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OperatingSystemVersionRangeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OperatingSystemVersionRange]] = Field(alias="value", default=None,)

from .operating_system_version_range import OperatingSystemVersionRange

