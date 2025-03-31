from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosNetworkUsageRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosNetworkUsageRule]] = Field(alias="value", default=None,)

from .ios_network_usage_rule import IosNetworkUsageRule
