from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsMedia(BaseModel):
	calleeDevice: Optional[CallRecordsDeviceInfo] = Field(alias="calleeDevice", default=None,)
	calleeNetwork: Optional[CallRecordsNetworkInfo] = Field(alias="calleeNetwork", default=None,)
	callerDevice: Optional[CallRecordsDeviceInfo] = Field(alias="callerDevice", default=None,)
	callerNetwork: Optional[CallRecordsNetworkInfo] = Field(alias="callerNetwork", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	streams: Optional[list[CallRecordsMediaStream]] = Field(alias="streams", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .call_records_device_info import CallRecordsDeviceInfo
from .call_records_network_info import CallRecordsNetworkInfo
from .call_records_device_info import CallRecordsDeviceInfo
from .call_records_network_info import CallRecordsNetworkInfo
from .call_records_media_stream import CallRecordsMediaStream

