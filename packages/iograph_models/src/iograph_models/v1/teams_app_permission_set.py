from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppPermissionSet(BaseModel):
	resourceSpecificPermissions: Optional[list[TeamsAppResourceSpecificPermission]] = Field(alias="resourceSpecificPermissions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_app_resource_specific_permission import TeamsAppResourceSpecificPermission

