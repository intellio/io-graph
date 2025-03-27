from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessFilteringPolicyLinkCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessFilteringPolicyLink]] = Field(alias="value", default=None,)

from .networkaccess_filtering_policy_link import NetworkaccessFilteringPolicyLink

