from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OpenNetworkAzureSecurityGroupFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OpenNetworkAzureSecurityGroupFinding]] = Field(alias="value", default=None,)

from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding

