from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupChatTeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	chatId: Optional[str] = Field(alias="chatId",default=None,)

from .teams_app_installation_scopes import TeamsAppInstallationScopes

