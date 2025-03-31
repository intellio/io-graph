from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultUserRoleOverrideCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DefaultUserRoleOverride]] = Field(alias="value", default=None,)

from .default_user_role_override import DefaultUserRoleOverride
