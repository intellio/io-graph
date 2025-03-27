from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppDashboardCardDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TeamsAppDashboardCardDefinition]] = Field(alias="value", default=None,)

from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition

