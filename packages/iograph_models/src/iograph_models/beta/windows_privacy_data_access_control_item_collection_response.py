from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsPrivacyDataAccessControlItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsPrivacyDataAccessControlItem]] = Field(alias="value", default=None,)

from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
