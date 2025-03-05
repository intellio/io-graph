from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppAuthorization(BaseModel):
	clientAppId: Optional[str] = Field(default=None,alias="clientAppId",)
	requiredPermissionSet: Optional[TeamsAppPermissionSet] = Field(default=None,alias="requiredPermissionSet",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .teams_app_permission_set import TeamsAppPermissionSet

