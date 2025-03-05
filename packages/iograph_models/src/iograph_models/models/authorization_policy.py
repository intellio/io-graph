from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	allowedToSignUpEmailBasedSubscriptions: Optional[bool] = Field(alias="allowedToSignUpEmailBasedSubscriptions",default=None,)
	allowedToUseSSPR: Optional[bool] = Field(alias="allowedToUseSSPR",default=None,)
	allowEmailVerifiedUsersToJoinOrganization: Optional[bool] = Field(alias="allowEmailVerifiedUsersToJoinOrganization",default=None,)
	allowInvitesFrom: Optional[AllowInvitesFrom | str] = Field(alias="allowInvitesFrom",default=None,)
	allowUserConsentForRiskyApps: Optional[bool] = Field(alias="allowUserConsentForRiskyApps",default=None,)
	blockMsolPowerShell: Optional[bool] = Field(alias="blockMsolPowerShell",default=None,)
	defaultUserRolePermissions: Optional[DefaultUserRolePermissions] = Field(alias="defaultUserRolePermissions",default=None,)
	guestUserRoleId: Optional[UUID] = Field(alias="guestUserRoleId",default=None,)

from .allow_invites_from import AllowInvitesFrom
from .default_user_role_permissions import DefaultUserRolePermissions

