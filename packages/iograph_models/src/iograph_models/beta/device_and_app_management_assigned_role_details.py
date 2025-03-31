from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceAndAppManagementAssignedRoleDetails(BaseModel):
	roleAssignmentIds: Optional[list[str]] = Field(alias="roleAssignmentIds", default=None,)
	roleDefinitionIds: Optional[list[str]] = Field(alias="roleDefinitionIds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

