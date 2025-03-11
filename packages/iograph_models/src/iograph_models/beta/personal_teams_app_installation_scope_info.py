from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersonalTeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)

from .teams_app_installation_scopes import TeamsAppInstallationScopes

