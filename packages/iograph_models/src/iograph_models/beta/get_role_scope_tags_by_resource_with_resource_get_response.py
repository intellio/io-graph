from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_role_scope_tags_by_resource_with_resourceGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[RoleScopeTag]] = Field(alias="value", default=None,)

from .role_scope_tag import RoleScopeTag

