from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OAuth2PermissionGrant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.oAuth2PermissionGrant"] = Field(alias="@odata.type",)
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	consentType: Optional[str] = Field(alias="consentType", default=None,)
	principalId: Optional[str] = Field(alias="principalId", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)

