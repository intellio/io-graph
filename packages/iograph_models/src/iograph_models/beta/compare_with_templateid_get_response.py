from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Compare_with_templateidGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementSettingComparison]] = Field(alias="value", default=None,)

from .device_management_setting_comparison import DeviceManagementSettingComparison
