from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserScopeTeamsAppInstallationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserScopeTeamsAppInstallation] = Field(alias="value",)

from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

