from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OutOfBoxExperienceSetting(BaseModel):
	deviceUsageType: Optional[WindowsDeviceUsageType] = Field(default=None,alias="deviceUsageType",)
	escapeLinkHidden: Optional[bool] = Field(default=None,alias="escapeLinkHidden",)
	eulaHidden: Optional[bool] = Field(default=None,alias="eulaHidden",)
	keyboardSelectionPageSkipped: Optional[bool] = Field(default=None,alias="keyboardSelectionPageSkipped",)
	privacySettingsHidden: Optional[bool] = Field(default=None,alias="privacySettingsHidden",)
	userType: Optional[WindowsUserType] = Field(default=None,alias="userType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .windows_device_usage_type import WindowsDeviceUsageType
from .windows_user_type import WindowsUserType

