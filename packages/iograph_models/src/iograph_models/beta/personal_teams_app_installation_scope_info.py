from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PersonalTeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope", default=None,)
	odata_type: Literal["#microsoft.graph.personalTeamsAppInstallationScopeInfo"] = Field(alias="@odata.type", default="#microsoft.graph.personalTeamsAppInstallationScopeInfo")
	userId: Optional[str] = Field(alias="userId", default=None,)

from .teams_app_installation_scopes import TeamsAppInstallationScopes
