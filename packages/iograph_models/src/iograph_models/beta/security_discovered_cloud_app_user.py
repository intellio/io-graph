from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityDiscoveredCloudAppUser(BaseModel):
	userIdentifier: Optional[str] = Field(alias="userIdentifier", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

