from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessFqdnFilteringRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessFqdnFilteringRule]] = Field(alias="value", default=None,)

from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule

