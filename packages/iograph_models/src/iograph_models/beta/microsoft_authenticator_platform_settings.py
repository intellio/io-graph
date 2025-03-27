from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAuthenticatorPlatformSettings(BaseModel):
	enforceAppPIN: Optional[EnforceAppPIN] = Field(alias="enforceAppPIN", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .enforce_app_p_i_n import EnforceAppPIN

