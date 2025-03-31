from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileAppPolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MobileAppPolicySetItem]] = Field(alias="value", default=None,)

from .mobile_app_policy_set_item import MobileAppPolicySetItem
