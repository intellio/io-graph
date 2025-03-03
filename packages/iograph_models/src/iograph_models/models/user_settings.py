from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	contributionToContentDiscoveryAsOrganizationDisabled: Optional[bool] = Field(default=None,alias="contributionToContentDiscoveryAsOrganizationDisabled",)
	contributionToContentDiscoveryDisabled: Optional[bool] = Field(default=None,alias="contributionToContentDiscoveryDisabled",)
	itemInsights: Optional[UserInsightsSettings] = Field(default=None,alias="itemInsights",)
	shiftPreferences: Optional[ShiftPreferences] = Field(default=None,alias="shiftPreferences",)
	storage: Optional[UserStorage] = Field(default=None,alias="storage",)
	windows: Optional[list[WindowsSetting]] = Field(default=None,alias="windows",)

from .user_insights_settings import UserInsightsSettings
from .shift_preferences import ShiftPreferences
from .user_storage import UserStorage
from .windows_setting import WindowsSetting

