from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PeopleAdminSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	itemInsights: Optional[InsightsSettings] = Field(default=None,alias="itemInsights",)
	profileCardProperties: Optional[list[ProfileCardProperty]] = Field(default=None,alias="profileCardProperties",)
	pronouns: Optional[PronounsSettings] = Field(default=None,alias="pronouns",)

from .insights_settings import InsightsSettings
from .profile_card_property import ProfileCardProperty
from .pronouns_settings import PronounsSettings

