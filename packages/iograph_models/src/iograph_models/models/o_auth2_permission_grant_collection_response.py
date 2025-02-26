from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OAuth2PermissionGrantCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OAuth2PermissionGrant] = Field(alias="value",)

from .o_auth2_permission_grant import OAuth2PermissionGrant

