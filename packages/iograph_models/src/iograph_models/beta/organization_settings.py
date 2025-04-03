from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OrganizationSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.organizationSettings"] = Field(alias="@odata.type", default="#microsoft.graph.organizationSettings")
	contactInsights: Optional[InsightsSettings] = Field(alias="contactInsights", default=None,)
	itemInsights: Optional[InsightsSettings] = Field(alias="itemInsights", default=None,)
	microsoftApplicationDataAccess: Optional[MicrosoftApplicationDataAccessSettings] = Field(alias="microsoftApplicationDataAccess", default=None,)
	peopleInsights: Optional[InsightsSettings] = Field(alias="peopleInsights", default=None,)

from .insights_settings import InsightsSettings
from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings
