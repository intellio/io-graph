from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkaccessDevice(BaseModel):
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isCompliant: Optional[bool] = Field(alias="isCompliant", default=None,)
	lastAccessDateTime: Optional[datetime] = Field(alias="lastAccessDateTime", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_traffic_type import NetworkaccessTrafficType
