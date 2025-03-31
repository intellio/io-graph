from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcAuditActor(BaseModel):
	applicationDisplayName: Optional[str] = Field(alias="applicationDisplayName", default=None,)
	applicationId: Optional[str] = Field(alias="applicationId", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	remoteTenantId: Optional[str] = Field(alias="remoteTenantId", default=None,)
	remoteUserId: Optional[str] = Field(alias="remoteUserId", default=None,)
	servicePrincipalName: Optional[str] = Field(alias="servicePrincipalName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPermissions: Optional[list[str]] = Field(alias="userPermissions", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	userRoleScopeTags: Optional[list[CloudPcUserRoleScopeTagInfo]] = Field(alias="userRoleScopeTags", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo
