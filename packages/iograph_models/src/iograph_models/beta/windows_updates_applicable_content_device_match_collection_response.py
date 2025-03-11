from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesApplicableContentDeviceMatchCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsUpdatesApplicableContentDeviceMatch]] = Field(alias="value",default=None,)

from .windows_updates_applicable_content_device_match import WindowsUpdatesApplicableContentDeviceMatch

