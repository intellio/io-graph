from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppIdentity(BaseModel):
	appId: Optional[str] = Field(default=None,alias="appId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	servicePrincipalId: Optional[str] = Field(default=None,alias="servicePrincipalId",)
	servicePrincipalName: Optional[str] = Field(default=None,alias="servicePrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


