from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamsAppSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsAppSettings"] = Field(alias="@odata.type", default="#microsoft.graph.teamsAppSettings")
	allowUserRequestsForAppAccess: Optional[bool] = Field(alias="allowUserRequestsForAppAccess", default=None,)
	customAppSettings: Optional[CustomAppSettings] = Field(alias="customAppSettings", default=None,)
	isChatResourceSpecificConsentEnabled: Optional[bool] = Field(alias="isChatResourceSpecificConsentEnabled", default=None,)
	isUserPersonalScopeResourceSpecificConsentEnabled: Optional[bool] = Field(alias="isUserPersonalScopeResourceSpecificConsentEnabled", default=None,)

from .custom_app_settings import CustomAppSettings
