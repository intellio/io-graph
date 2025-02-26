from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsSettingInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WindowsSettingInstance] = Field(alias="value",)

from .windows_setting_instance import WindowsSettingInstance

