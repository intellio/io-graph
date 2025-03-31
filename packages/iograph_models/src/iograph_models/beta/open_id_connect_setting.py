from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OpenIdConnectSetting(BaseModel):
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	discoveryUrl: Optional[str] = Field(alias="discoveryUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

