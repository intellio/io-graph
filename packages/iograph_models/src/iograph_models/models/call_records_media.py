from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsMedia(BaseModel):
	calleeDevice: Optional[CallRecordsDeviceInfo] = Field(default=None,alias="calleeDevice",)
	calleeNetwork: Optional[CallRecordsNetworkInfo] = Field(default=None,alias="calleeNetwork",)
	callerDevice: Optional[CallRecordsDeviceInfo] = Field(default=None,alias="callerDevice",)
	callerNetwork: Optional[CallRecordsNetworkInfo] = Field(default=None,alias="callerNetwork",)
	label: Optional[str] = Field(default=None,alias="label",)
	streams: list[CallRecordsMediaStream] = Field(alias="streams",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_device_info import CallRecordsDeviceInfo
from .call_records_network_info import CallRecordsNetworkInfo
from .call_records_device_info import CallRecordsDeviceInfo
from .call_records_network_info import CallRecordsNetworkInfo
from .call_records_media_stream import CallRecordsMediaStream

