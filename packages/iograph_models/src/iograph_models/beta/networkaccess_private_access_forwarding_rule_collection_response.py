from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessPrivateAccessForwardingRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessPrivateAccessForwardingRule]] = Field(alias="value", default=None,)

from .networkaccess_private_access_forwarding_rule import NetworkaccessPrivateAccessForwardingRule
