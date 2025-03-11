from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessM365ForwardingRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NetworkaccessM365ForwardingRule]] = Field(alias="value",default=None,)

from .networkaccess_m365_forwarding_rule import NetworkaccessM365ForwardingRule

