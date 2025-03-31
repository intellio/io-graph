from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GroupChatTeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope", default=None,)
	odata_type: Literal["#microsoft.graph.groupChatTeamsAppInstallationScopeInfo"] = Field(alias="@odata.type", default="#microsoft.graph.groupChatTeamsAppInstallationScopeInfo")
	chatId: Optional[str] = Field(alias="chatId", default=None,)

from .teams_app_installation_scopes import TeamsAppInstallationScopes
