from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DefaultUserRolePermissions(BaseModel):
	allowedToCreateApps: Optional[bool] = Field(alias="allowedToCreateApps",default=None,)
	allowedToCreateSecurityGroups: Optional[bool] = Field(alias="allowedToCreateSecurityGroups",default=None,)
	allowedToCreateTenants: Optional[bool] = Field(alias="allowedToCreateTenants",default=None,)
	allowedToReadBitlockerKeysForOwnedDevice: Optional[bool] = Field(alias="allowedToReadBitlockerKeysForOwnedDevice",default=None,)
	allowedToReadOtherUsers: Optional[bool] = Field(alias="allowedToReadOtherUsers",default=None,)
	permissionGrantPoliciesAssigned: Optional[list[str]] = Field(alias="permissionGrantPoliciesAssigned",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


