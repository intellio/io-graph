from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkaccessRemoteNetworkHealthEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.remoteNetworkHealthEvent"] = Field(alias="@odata.type",)
	bgpRoutesAdvertisedCount: Optional[int] = Field(alias="bgpRoutesAdvertisedCount", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	destinationIp: Optional[str] = Field(alias="destinationIp", default=None,)
	receivedBytes: Optional[int] = Field(alias="receivedBytes", default=None,)
	remoteNetworkId: Optional[str] = Field(alias="remoteNetworkId", default=None,)
	sentBytes: Optional[int] = Field(alias="sentBytes", default=None,)
	sourceIp: Optional[str] = Field(alias="sourceIp", default=None,)
	status: Optional[NetworkaccessRemoteNetworkStatus | str] = Field(alias="status", default=None,)

from .networkaccess_remote_network_status import NetworkaccessRemoteNetworkStatus
