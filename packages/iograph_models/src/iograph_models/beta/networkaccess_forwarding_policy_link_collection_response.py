from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessForwardingPolicyLinkCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessForwardingPolicyLink]] = Field(alias="value", default=None,)

from .networkaccess_forwarding_policy_link import NetworkaccessForwardingPolicyLink
