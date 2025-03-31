from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcHealthCheckItem(BaseModel):
	additionalDetails: Optional[str] = Field(alias="additionalDetails", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastHealthCheckDateTime: Optional[datetime] = Field(alias="lastHealthCheckDateTime", default=None,)
	result: Optional[CloudPcConnectivityEventResult | str] = Field(alias="result", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_connectivity_event_result import CloudPcConnectivityEventResult
