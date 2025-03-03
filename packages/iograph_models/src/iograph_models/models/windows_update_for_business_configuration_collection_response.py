from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdateForBusinessConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WindowsUpdateForBusinessConfiguration]] = Field(default=None,alias="value",)

from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

