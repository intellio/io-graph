from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	allowedToSignUpEmailBasedSubscriptions: Optional[bool] = Field(default=None,alias="allowedToSignUpEmailBasedSubscriptions",)
	allowedToUseSSPR: Optional[bool] = Field(default=None,alias="allowedToUseSSPR",)
	allowEmailVerifiedUsersToJoinOrganization: Optional[bool] = Field(default=None,alias="allowEmailVerifiedUsersToJoinOrganization",)
	allowInvitesFrom: Optional[AllowInvitesFrom] = Field(default=None,alias="allowInvitesFrom",)
	allowUserConsentForRiskyApps: Optional[bool] = Field(default=None,alias="allowUserConsentForRiskyApps",)
	blockMsolPowerShell: Optional[bool] = Field(default=None,alias="blockMsolPowerShell",)
	defaultUserRolePermissions: Optional[DefaultUserRolePermissions] = Field(default=None,alias="defaultUserRolePermissions",)
	guestUserRoleId: Optional[UUID] = Field(default=None,alias="guestUserRoleId",)

from .allow_invites_from import AllowInvitesFrom
from .default_user_role_permissions import DefaultUserRolePermissions

