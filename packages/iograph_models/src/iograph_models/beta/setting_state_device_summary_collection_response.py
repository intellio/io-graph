from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SettingStateDeviceSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SettingStateDeviceSummary]] = Field(alias="value",default=None,)

from .setting_state_device_summary import SettingStateDeviceSummary

