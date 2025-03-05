from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcAuditActor(BaseModel):
	applicationDisplayName: Optional[str] = Field(default=None,alias="applicationDisplayName",)
	applicationId: Optional[str] = Field(default=None,alias="applicationId",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	remoteTenantId: Optional[str] = Field(default=None,alias="remoteTenantId",)
	remoteUserId: Optional[str] = Field(default=None,alias="remoteUserId",)
	servicePrincipalName: Optional[str] = Field(default=None,alias="servicePrincipalName",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userPermissions: Optional[list[str]] = Field(default=None,alias="userPermissions",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	userRoleScopeTags: Optional[list[CloudPcUserRoleScopeTagInfo]] = Field(default=None,alias="userRoleScopeTags",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo

