from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessCrossTenantAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.crossTenantAccessSettings"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.crossTenantAccessSettings")
	networkPacketTaggingStatus: Optional[NetworkaccessStatus | str] = Field(alias="networkPacketTaggingStatus", default=None,)

from .networkaccess_status import NetworkaccessStatus
