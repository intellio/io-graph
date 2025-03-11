from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutOfBoxExperienceSettings(BaseModel):
	deviceUsageType: Optional[WindowsDeviceUsageType | str] = Field(alias="deviceUsageType",default=None,)
	hideEscapeLink: Optional[bool] = Field(alias="hideEscapeLink",default=None,)
	hideEULA: Optional[bool] = Field(alias="hideEULA",default=None,)
	hidePrivacySettings: Optional[bool] = Field(alias="hidePrivacySettings",default=None,)
	skipKeyboardSelectionPage: Optional[bool] = Field(alias="skipKeyboardSelectionPage",default=None,)
	userType: Optional[WindowsUserType | str] = Field(alias="userType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_device_usage_type import WindowsDeviceUsageType
from .windows_user_type import WindowsUserType

