from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OAuthConsentAppDetail(BaseModel):
	appScope: Optional[OAuthAppScope | str] = Field(alias="appScope", default=None,)
	displayLogo: Optional[str] = Field(alias="displayLogo", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .o_auth_app_scope import OAuthAppScope

