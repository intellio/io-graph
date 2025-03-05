from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OAuth2PermissionGrant(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientId: Optional[str] = Field(default=None,alias="clientId",)
	consentType: Optional[str] = Field(default=None,alias="consentType",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	scope: Optional[str] = Field(default=None,alias="scope",)


