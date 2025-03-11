from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamTeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	teamId: Optional[str] = Field(alias="teamId",default=None,)

from .teams_app_installation_scopes import TeamsAppInstallationScopes

