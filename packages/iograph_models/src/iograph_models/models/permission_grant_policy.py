from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PermissionGrantPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	excludes: list[PermissionGrantConditionSet] = Field(alias="excludes",)
	includes: list[PermissionGrantConditionSet] = Field(alias="includes",)

from .permission_grant_condition_set import PermissionGrantConditionSet
from .permission_grant_condition_set import PermissionGrantConditionSet

