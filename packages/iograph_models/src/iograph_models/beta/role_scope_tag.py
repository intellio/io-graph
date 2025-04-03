from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RoleScopeTag(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.roleScopeTag"] = Field(alias="@odata.type", default="#microsoft.graph.roleScopeTag")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	permissions: Optional[list[str]] = Field(alias="permissions", default=None,)
	assignments: Optional[list[RoleScopeTagAutoAssignment]] = Field(alias="assignments", default=None,)

from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment
