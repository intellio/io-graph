from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppAuthorization(BaseModel):
	clientAppId: Optional[str] = Field(alias="clientAppId", default=None,)
	requiredPermissionSet: Optional[TeamsAppPermissionSet] = Field(alias="requiredPermissionSet", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_app_permission_set import TeamsAppPermissionSet
