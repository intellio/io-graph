from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OAuth2PermissionGrantCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[OAuth2PermissionGrant]] = Field(alias="value",default=None,)

from .o_auth2_permission_grant import OAuth2PermissionGrant

