from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowUserRequestsForAppAccess: Optional[bool] = Field(alias="allowUserRequestsForAppAccess",default=None,)
	customAppSettings: Optional[CustomAppSettings] = Field(alias="customAppSettings",default=None,)
	isChatResourceSpecificConsentEnabled: Optional[bool] = Field(alias="isChatResourceSpecificConsentEnabled",default=None,)
	isUserPersonalScopeResourceSpecificConsentEnabled: Optional[bool] = Field(alias="isUserPersonalScopeResourceSpecificConsentEnabled",default=None,)

from .custom_app_settings import CustomAppSettings

