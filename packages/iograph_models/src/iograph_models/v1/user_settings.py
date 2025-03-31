from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userSettings"] = Field(alias="@odata.type",)
	contributionToContentDiscoveryAsOrganizationDisabled: Optional[bool] = Field(alias="contributionToContentDiscoveryAsOrganizationDisabled", default=None,)
	contributionToContentDiscoveryDisabled: Optional[bool] = Field(alias="contributionToContentDiscoveryDisabled", default=None,)
	itemInsights: Optional[UserInsightsSettings] = Field(alias="itemInsights", default=None,)
	shiftPreferences: Optional[ShiftPreferences] = Field(alias="shiftPreferences", default=None,)
	storage: Optional[UserStorage] = Field(alias="storage", default=None,)
	windows: Optional[list[WindowsSetting]] = Field(alias="windows", default=None,)

from .user_insights_settings import UserInsightsSettings
from .shift_preferences import ShiftPreferences
from .user_storage import UserStorage
from .windows_setting import WindowsSetting
