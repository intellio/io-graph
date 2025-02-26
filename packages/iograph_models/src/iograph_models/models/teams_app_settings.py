from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowUserRequestsForAppAccess: Optional[bool] = Field(default=None,alias="allowUserRequestsForAppAccess",)
	isUserPersonalScopeResourceSpecificConsentEnabled: Optional[bool] = Field(default=None,alias="isUserPersonalScopeResourceSpecificConsentEnabled",)


