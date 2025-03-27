from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authorizationPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.authorizationPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	allowedToSignUpEmailBasedSubscriptions: Optional[bool] = Field(alias="allowedToSignUpEmailBasedSubscriptions", default=None,)
	allowedToUseSSPR: Optional[bool] = Field(alias="allowedToUseSSPR", default=None,)
	allowEmailVerifiedUsersToJoinOrganization: Optional[bool] = Field(alias="allowEmailVerifiedUsersToJoinOrganization", default=None,)
	allowInvitesFrom: Optional[AllowInvitesFrom | str] = Field(alias="allowInvitesFrom", default=None,)
	allowUserConsentForRiskyApps: Optional[bool] = Field(alias="allowUserConsentForRiskyApps", default=None,)
	blockMsolPowerShell: Optional[bool] = Field(alias="blockMsolPowerShell", default=None,)
	defaultUserRolePermissions: Optional[DefaultUserRolePermissions] = Field(alias="defaultUserRolePermissions", default=None,)
	enabledPreviewFeatures: Optional[list[str]] = Field(alias="enabledPreviewFeatures", default=None,)
	guestUserRoleId: Optional[UUID] = Field(alias="guestUserRoleId", default=None,)
	permissionGrantPolicyIdsAssignedToDefaultUserRole: Optional[list[str]] = Field(alias="permissionGrantPolicyIdsAssignedToDefaultUserRole", default=None,)
	defaultUserRoleOverrides: Optional[list[DefaultUserRoleOverride]] = Field(alias="defaultUserRoleOverrides", default=None,)

from .allow_invites_from import AllowInvitesFrom
from .default_user_role_permissions import DefaultUserRolePermissions
from .default_user_role_override import DefaultUserRoleOverride

