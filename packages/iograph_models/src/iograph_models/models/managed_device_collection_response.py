from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedDevice] = Field(alias="value",)

from .managed_device import ManagedDevice

