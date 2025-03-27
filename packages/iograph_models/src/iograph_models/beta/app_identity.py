from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppIdentity(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId", default=None,)
	servicePrincipalName: Optional[str] = Field(alias="servicePrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


