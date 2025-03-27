from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementAssignedRoleDefinition(BaseModel):
	permissions: Optional[list[str]] = Field(alias="permissions", default=None,)
	roleDefinitionDisplayName: Optional[str] = Field(alias="roleDefinitionDisplayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


