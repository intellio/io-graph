from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppResourceSpecificPermission(BaseModel):
	permissionType: Optional[TeamsAppResourceSpecificPermissionType | str] = Field(alias="permissionType", default=None,)
	permissionValue: Optional[str] = Field(alias="permissionValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_app_resource_specific_permission_type import TeamsAppResourceSpecificPermissionType
