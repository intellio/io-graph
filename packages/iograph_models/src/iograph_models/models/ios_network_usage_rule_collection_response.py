from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosNetworkUsageRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosNetworkUsageRule] = Field(alias="value",)

from .ios_network_usage_rule import IosNetworkUsageRule

