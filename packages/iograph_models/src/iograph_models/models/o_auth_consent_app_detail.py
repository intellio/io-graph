from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OAuthConsentAppDetail(BaseModel):
	appScope: Optional[OAuthAppScope] = Field(default=None,alias="appScope",)
	displayLogo: Optional[str] = Field(default=None,alias="displayLogo",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .o_auth_app_scope import OAuthAppScope

