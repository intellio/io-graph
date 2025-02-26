from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsNetworkInfo(BaseModel):
	bandwidthLowEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	basicServiceSetIdentifier: Optional[str] = Field(default=None,alias="basicServiceSetIdentifier",)
	connectionType: Optional[CallRecordsNetworkConnectionType] = Field(default=None,alias="connectionType",)
	delayEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	dnsSuffix: Optional[str] = Field(default=None,alias="dnsSuffix",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	linkSpeed: Optional[int] = Field(default=None,alias="linkSpeed",)
	macAddress: Optional[str] = Field(default=None,alias="macAddress",)
	networkTransportProtocol: Optional[CallRecordsNetworkTransportProtocol] = Field(default=None,alias="networkTransportProtocol",)
	port: Optional[int] = Field(default=None,alias="port",)
	receivedQualityEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	reflexiveIPAddress: Optional[str] = Field(default=None,alias="reflexiveIPAddress",)
	relayIPAddress: Optional[str] = Field(default=None,alias="relayIPAddress",)
	relayPort: Optional[int] = Field(default=None,alias="relayPort",)
	sentQualityEventRatio: Optional[float] | Optional[str] | ReferenceNumeric
	subnet: Optional[str] = Field(default=None,alias="subnet",)
	traceRouteHops: list[CallRecordsTraceRouteHop] = Field(alias="traceRouteHops",)
	wifiBand: Optional[CallRecordsWifiBand] = Field(default=None,alias="wifiBand",)
	wifiBatteryCharge: Optional[int] = Field(default=None,alias="wifiBatteryCharge",)
	wifiChannel: Optional[int] = Field(default=None,alias="wifiChannel",)
	wifiMicrosoftDriver: Optional[str] = Field(default=None,alias="wifiMicrosoftDriver",)
	wifiMicrosoftDriverVersion: Optional[str] = Field(default=None,alias="wifiMicrosoftDriverVersion",)
	wifiRadioType: Optional[CallRecordsWifiRadioType] = Field(default=None,alias="wifiRadioType",)
	wifiSignalStrength: Optional[int] = Field(default=None,alias="wifiSignalStrength",)
	wifiVendorDriver: Optional[str] = Field(default=None,alias="wifiVendorDriver",)
	wifiVendorDriverVersion: Optional[str] = Field(default=None,alias="wifiVendorDriverVersion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .call_records_network_connection_type import CallRecordsNetworkConnectionType
from .reference_numeric import ReferenceNumeric
from .call_records_network_transport_protocol import CallRecordsNetworkTransportProtocol
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .call_records_trace_route_hop import CallRecordsTraceRouteHop
from .call_records_wifi_band import CallRecordsWifiBand
from .call_records_wifi_radio_type import CallRecordsWifiRadioType

