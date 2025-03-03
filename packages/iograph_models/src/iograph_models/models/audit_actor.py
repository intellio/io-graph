from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditActor(BaseModel):
	applicationDisplayName: Optional[str] = Field(default=None,alias="applicationDisplayName",)
	applicationId: Optional[str] = Field(default=None,alias="applicationId",)
	auditActorType: Optional[str] = Field(default=None,alias="auditActorType",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	servicePrincipalName: Optional[str] = Field(default=None,alias="servicePrincipalName",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userPermissions: Optional[list[str]] = Field(default=None,alias="userPermissions",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


