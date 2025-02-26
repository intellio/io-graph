from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionResourceCollectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WindowsInformationProtectionResourceCollection] = Field(alias="value",)

from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection

