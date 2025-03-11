from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuditUserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	homeTenantId: Optional[str] = Field(alias="homeTenantId",default=None,)
	homeTenantName: Optional[str] = Field(alias="homeTenantName",default=None,)


