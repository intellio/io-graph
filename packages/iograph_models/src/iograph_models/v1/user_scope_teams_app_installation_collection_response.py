from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserScopeTeamsAppInstallationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserScopeTeamsAppInstallation]] = Field(alias="value", default=None,)

from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
