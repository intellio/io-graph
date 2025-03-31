from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows_privacy_access_controlsPostRequest(BaseModel):
	windowsPrivacyAccessControls: Optional[list[WindowsPrivacyDataAccessControlItem]] = Field(alias="windowsPrivacyAccessControls", default=None,)

from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
