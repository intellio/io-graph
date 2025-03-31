from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessLocalConnectivityConfiguration(BaseModel):
	asn: Optional[int] = Field(alias="asn", default=None,)
	bgpAddress: Optional[str] = Field(alias="bgpAddress", default=None,)
	endpoint: Optional[str] = Field(alias="endpoint", default=None,)
	region: Optional[NetworkaccessRegion | str] = Field(alias="region", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_region import NetworkaccessRegion
