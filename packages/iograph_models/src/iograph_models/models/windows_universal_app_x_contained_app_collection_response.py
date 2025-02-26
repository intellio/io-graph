from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUniversalAppXContainedAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WindowsUniversalAppXContainedApp] = Field(alias="value",)

from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp

