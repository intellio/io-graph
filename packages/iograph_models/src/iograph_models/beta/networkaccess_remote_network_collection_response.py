from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRemoteNetworkCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NetworkaccessRemoteNetwork]] = Field(alias="value",default=None,)

from .networkaccess_remote_network import NetworkaccessRemoteNetwork

