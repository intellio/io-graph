from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppResourceSpecificPermissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TeamsAppResourceSpecificPermission] = Field(alias="value",)

from .teams_app_resource_specific_permission import TeamsAppResourceSpecificPermission

