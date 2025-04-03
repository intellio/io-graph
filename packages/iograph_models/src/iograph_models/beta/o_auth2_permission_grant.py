from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OAuth2PermissionGrant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.oAuth2PermissionGrant"] = Field(alias="@odata.type", default="#microsoft.graph.oAuth2PermissionGrant")
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	consentType: Optional[str] = Field(alias="consentType", default=None,)
	expiryTime: Optional[datetime] = Field(alias="expiryTime", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)
	startTime: Optional[datetime] = Field(alias="startTime", default=None,)

