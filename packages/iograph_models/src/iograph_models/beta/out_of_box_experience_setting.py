from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutOfBoxExperienceSetting(BaseModel):
	deviceUsageType: Optional[WindowsDeviceUsageType | str] = Field(alias="deviceUsageType", default=None,)
	escapeLinkHidden: Optional[bool] = Field(alias="escapeLinkHidden", default=None,)
	eulaHidden: Optional[bool] = Field(alias="eulaHidden", default=None,)
	keyboardSelectionPageSkipped: Optional[bool] = Field(alias="keyboardSelectionPageSkipped", default=None,)
	privacySettingsHidden: Optional[bool] = Field(alias="privacySettingsHidden", default=None,)
	userType: Optional[WindowsUserType | str] = Field(alias="userType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_device_usage_type import WindowsDeviceUsageType
from .windows_user_type import WindowsUserType

