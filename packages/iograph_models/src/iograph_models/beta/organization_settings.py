from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OrganizationSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contactInsights: Optional[InsightsSettings] = Field(alias="contactInsights",default=None,)
	itemInsights: Optional[InsightsSettings] = Field(alias="itemInsights",default=None,)
	microsoftApplicationDataAccess: Optional[MicrosoftApplicationDataAccessSettings] = Field(alias="microsoftApplicationDataAccess",default=None,)
	peopleInsights: Optional[InsightsSettings] = Field(alias="peopleInsights",default=None,)

from .insights_settings import InsightsSettings
from .insights_settings import InsightsSettings
from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings
from .insights_settings import InsightsSettings

