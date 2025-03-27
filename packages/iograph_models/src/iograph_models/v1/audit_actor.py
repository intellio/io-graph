from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuditActor(BaseModel):
	applicationDisplayName: Optional[str] = Field(alias="applicationDisplayName", default=None,)
	applicationId: Optional[str] = Field(alias="applicationId", default=None,)
	auditActorType: Optional[str] = Field(alias="auditActorType", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	servicePrincipalName: Optional[str] = Field(alias="servicePrincipalName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPermissions: Optional[list[str]] = Field(alias="userPermissions", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


