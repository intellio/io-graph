from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ScopedRoleMembershipCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ScopedRoleMembership] = Field(alias="value",)

from .scoped_role_membership import ScopedRoleMembership

