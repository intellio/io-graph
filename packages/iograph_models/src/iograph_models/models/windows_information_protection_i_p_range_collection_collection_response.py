from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionIPRangeCollectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WindowsInformationProtectionIPRangeCollection]] = Field(default=None,alias="value",)

from .windows_information_protection_i_p_range_collection import WindowsInformationProtectionIPRangeCollection

