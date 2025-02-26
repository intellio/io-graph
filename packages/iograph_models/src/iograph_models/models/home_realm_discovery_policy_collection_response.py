from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class HomeRealmDiscoveryPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[HomeRealmDiscoveryPolicy] = Field(alias="value",)

from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

