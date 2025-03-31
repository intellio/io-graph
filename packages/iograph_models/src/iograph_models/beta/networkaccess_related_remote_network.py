from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessRelatedRemoteNetwork(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedRemoteNetwork"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedRemoteNetwork")
	remoteNetworkId: Optional[str] = Field(alias="remoteNetworkId", default=None,)

