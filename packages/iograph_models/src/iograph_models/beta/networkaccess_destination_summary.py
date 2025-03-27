from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessDestinationSummary(BaseModel):
	count: Optional[int] = Field(alias="count", default=None,)
	destination: Optional[str] = Field(alias="destination", default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_traffic_type import NetworkaccessTrafficType

