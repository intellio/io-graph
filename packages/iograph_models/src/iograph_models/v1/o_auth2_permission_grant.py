from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OAuth2PermissionGrant(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	clientId: Optional[str] = Field(alias="clientId",default=None,)
	consentType: Optional[str] = Field(alias="consentType",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	scope: Optional[str] = Field(alias="scope",default=None,)


