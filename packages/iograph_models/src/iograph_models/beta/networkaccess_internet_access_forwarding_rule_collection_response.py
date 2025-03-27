from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessInternetAccessForwardingRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessInternetAccessForwardingRule]] = Field(alias="value", default=None,)

from .networkaccess_internet_access_forwarding_rule import NetworkaccessInternetAccessForwardingRule

