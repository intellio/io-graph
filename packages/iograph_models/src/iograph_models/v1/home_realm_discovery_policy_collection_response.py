from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HomeRealmDiscoveryPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[HomeRealmDiscoveryPolicy]] = Field(alias="value", default=None,)

from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

