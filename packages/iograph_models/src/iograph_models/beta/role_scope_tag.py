from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoleScopeTag(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	permissions: Optional[list[str]] = Field(alias="permissions", default=None,)
	assignments: Optional[list[RoleScopeTagAutoAssignment]] = Field(alias="assignments", default=None,)

from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment

