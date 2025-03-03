from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SettingStateDeviceSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="value",)

from .setting_state_device_summary import SettingStateDeviceSummary

