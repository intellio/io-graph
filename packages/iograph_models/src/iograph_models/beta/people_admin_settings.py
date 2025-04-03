from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PeopleAdminSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.peopleAdminSettings"] = Field(alias="@odata.type", default="#microsoft.graph.peopleAdminSettings")
	itemInsights: Optional[InsightsSettings] = Field(alias="itemInsights", default=None,)
	namePronunciation: Optional[NamePronunciationSettings] = Field(alias="namePronunciation", default=None,)
	profileCardProperties: Optional[list[ProfileCardProperty]] = Field(alias="profileCardProperties", default=None,)
	pronouns: Optional[PronounsSettings] = Field(alias="pronouns", default=None,)

from .insights_settings import InsightsSettings
from .name_pronunciation_settings import NamePronunciationSettings
from .profile_card_property import ProfileCardProperty
from .pronouns_settings import PronounsSettings
