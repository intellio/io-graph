from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuditUserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.auditUserIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.auditUserIdentity")
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	homeTenantId: Optional[str] = Field(alias="homeTenantId", default=None,)
	homeTenantName: Optional[str] = Field(alias="homeTenantName", default=None,)

