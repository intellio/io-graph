from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppDashboardCardDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentSource: Optional[TeamsAppDashboardCardContentSource] = Field(alias="contentSource",default=None,)
	defaultSize: Optional[TeamsAppDashboardCardSize | str] = Field(alias="defaultSize",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	icon: Optional[TeamsAppDashboardCardIcon] = Field(alias="icon",default=None,)
	pickerGroupId: Optional[str] = Field(alias="pickerGroupId",default=None,)

from .teams_app_dashboard_card_content_source import TeamsAppDashboardCardContentSource
from .teams_app_dashboard_card_size import TeamsAppDashboardCardSize
from .teams_app_dashboard_card_icon import TeamsAppDashboardCardIcon

