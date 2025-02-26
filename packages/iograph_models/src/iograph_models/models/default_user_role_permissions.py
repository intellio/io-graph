from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultUserRolePermissions(BaseModel):
	allowedToCreateApps: Optional[bool] = Field(default=None,alias="allowedToCreateApps",)
	allowedToCreateSecurityGroups: Optional[bool] = Field(default=None,alias="allowedToCreateSecurityGroups",)
	allowedToCreateTenants: Optional[bool] = Field(default=None,alias="allowedToCreateTenants",)
	allowedToReadBitlockerKeysForOwnedDevice: Optional[bool] = Field(default=None,alias="allowedToReadBitlockerKeysForOwnedDevice",)
	allowedToReadOtherUsers: Optional[bool] = Field(default=None,alias="allowedToReadOtherUsers",)
	permissionGrantPoliciesAssigned: list[Optional[str]] = Field(alias="permissionGrantPoliciesAssigned",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


