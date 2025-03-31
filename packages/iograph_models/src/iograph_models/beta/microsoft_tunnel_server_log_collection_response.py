from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MicrosoftTunnelServerLogCollectionResponse(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftTunnelServerLogCollectionResponse"] = Field(alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	expiryDateTime: Optional[datetime] = Field(alias="expiryDateTime", default=None,)
	requestDateTime: Optional[datetime] = Field(alias="requestDateTime", default=None,)
	serverId: Optional[str] = Field(alias="serverId", default=None,)
	sizeInBytes: Optional[int] = Field(alias="sizeInBytes", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[MicrosoftTunnelLogCollectionStatus | str] = Field(alias="status", default=None,)

from .microsoft_tunnel_log_collection_status import MicrosoftTunnelLogCollectionStatus
