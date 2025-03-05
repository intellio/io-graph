from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionGrantPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	excludes: Optional[list[PermissionGrantConditionSet]] = Field(default=None,alias="excludes",)
	includes: Optional[list[PermissionGrantConditionSet]] = Field(default=None,alias="includes",)

from .permission_grant_condition_set import PermissionGrantConditionSet
from .permission_grant_condition_set import PermissionGrantConditionSet

