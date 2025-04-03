from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userSettings"] = Field(alias="@odata.type", default="#microsoft.graph.userSettings")
	contributionToContentDiscoveryAsOrganizationDisabled: Optional[bool] = Field(alias="contributionToContentDiscoveryAsOrganizationDisabled", default=None,)
	contributionToContentDiscoveryDisabled: Optional[bool] = Field(alias="contributionToContentDiscoveryDisabled", default=None,)
	contactMergeSuggestions: Optional[ContactMergeSuggestions] = Field(alias="contactMergeSuggestions", default=None,)
	exchange: Optional[ExchangeSettings] = Field(alias="exchange", default=None,)
	itemInsights: Optional[UserInsightsSettings] = Field(alias="itemInsights", default=None,)
	regionalAndLanguageSettings: Optional[RegionalAndLanguageSettings] = Field(alias="regionalAndLanguageSettings", default=None,)
	shiftPreferences: Optional[ShiftPreferences] = Field(alias="shiftPreferences", default=None,)
	storage: Optional[UserStorage] = Field(alias="storage", default=None,)
	windows: Optional[list[WindowsSetting]] = Field(alias="windows", default=None,)

from .contact_merge_suggestions import ContactMergeSuggestions
from .exchange_settings import ExchangeSettings
from .user_insights_settings import UserInsightsSettings
from .regional_and_language_settings import RegionalAndLanguageSettings
from .shift_preferences import ShiftPreferences
from .user_storage import UserStorage
from .windows_setting import WindowsSetting
