from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessLocalConnectivityConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NetworkaccessLocalConnectivityConfiguration]] = Field(alias="value",default=None,)

from .networkaccess_local_connectivity_configuration import NetworkaccessLocalConnectivityConfiguration

