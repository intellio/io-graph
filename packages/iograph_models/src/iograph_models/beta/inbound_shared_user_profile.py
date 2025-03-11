from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InboundSharedUserProfile(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	homeTenantId: Optional[str] = Field(alias="homeTenantId",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


