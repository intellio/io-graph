from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[RoleScopeTagAutoAssignment]] = Field(alias="value",default=None,)

from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment

