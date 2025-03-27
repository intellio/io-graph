from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessEntitiesSummary(BaseModel):
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	workloadCount: Optional[int] = Field(alias="workloadCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_traffic_type import NetworkaccessTrafficType

