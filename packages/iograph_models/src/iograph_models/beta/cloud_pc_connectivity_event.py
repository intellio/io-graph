from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcConnectivityEvent(BaseModel):
	activityId: Optional[str] = Field(alias="activityId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	eventResult: Optional[CloudPcConnectivityEventResult | str] = Field(alias="eventResult", default=None,)
	eventType: Optional[CloudPcConnectivityEventType | str] = Field(alias="eventType", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_connectivity_event_result import CloudPcConnectivityEventResult
from .cloud_pc_connectivity_event_type import CloudPcConnectivityEventType

