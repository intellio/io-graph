from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)


