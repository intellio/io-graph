from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionResourceCollectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="value", default=None,)

from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
