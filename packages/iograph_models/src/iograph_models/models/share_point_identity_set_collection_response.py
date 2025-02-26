from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharePointIdentitySetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SharePointIdentitySet] = Field(alias="value",)

from .share_point_identity_set import SharePointIdentitySet

