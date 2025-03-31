from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharePointProtectionPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SharePointProtectionPolicy]] = Field(alias="value", default=None,)

from .share_point_protection_policy import SharePointProtectionPolicy
