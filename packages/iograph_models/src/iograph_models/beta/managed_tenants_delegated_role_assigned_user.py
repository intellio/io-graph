from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsDelegatedRoleAssignedUser(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	userEntityId: Optional[str] = Field(alias="userEntityId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


