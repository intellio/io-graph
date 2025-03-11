from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionGrantPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	includeAllPreApprovedApplications: Optional[bool] = Field(alias="includeAllPreApprovedApplications",default=None,)
	resourceScopeType: Optional[ResourceScopeType | str] = Field(alias="resourceScopeType",default=None,)
	excludes: Optional[list[PermissionGrantConditionSet]] = Field(alias="excludes",default=None,)
	includes: Optional[list[PermissionGrantConditionSet]] = Field(alias="includes",default=None,)

from .resource_scope_type import ResourceScopeType
from .permission_grant_condition_set import PermissionGrantConditionSet
from .permission_grant_condition_set import PermissionGrantConditionSet

