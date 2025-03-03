from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppPermissionSet(BaseModel):
	resourceSpecificPermissions: Optional[list[TeamsAppResourceSpecificPermission]] = Field(default=None,alias="resourceSpecificPermissions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .teams_app_resource_specific_permission import TeamsAppResourceSpecificPermission

