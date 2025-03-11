from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRedundancyConfiguration(BaseModel):
	redundancyTier: Optional[NetworkaccessRedundancyTier | str] = Field(alias="redundancyTier",default=None,)
	zoneLocalIpAddress: Optional[str] = Field(alias="zoneLocalIpAddress",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_redundancy_tier import NetworkaccessRedundancyTier

