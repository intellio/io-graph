from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppResourceSpecificPermission(BaseModel):
	permissionType: Optional[TeamsAppResourceSpecificPermissionType] = Field(default=None,alias="permissionType",)
	permissionValue: Optional[str] = Field(default=None,alias="permissionValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .teams_app_resource_specific_permission_type import TeamsAppResourceSpecificPermissionType

