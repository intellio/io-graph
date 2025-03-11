from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsNetworkInfo(BaseModel):
	bandwidthLowEventRatio: float | str | ReferenceNumeric
	basicServiceSetIdentifier: Optional[str] = Field(alias="basicServiceSetIdentifier",default=None,)
	connectionType: Optional[CallRecordsNetworkConnectionType | str] = Field(alias="connectionType",default=None,)
	delayEventRatio: float | str | ReferenceNumeric
	dnsSuffix: Optional[str] = Field(alias="dnsSuffix",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	linkSpeed: Optional[int] = Field(alias="linkSpeed",default=None,)
	macAddress: Optional[str] = Field(alias="macAddress",default=None,)
	networkTransportProtocol: Optional[CallRecordsNetworkTransportProtocol | str] = Field(alias="networkTransportProtocol",default=None,)
	port: Optional[int] = Field(alias="port",default=None,)
	receivedQualityEventRatio: float | str | ReferenceNumeric
	reflexiveIPAddress: Optional[str] = Field(alias="reflexiveIPAddress",default=None,)
	relayIPAddress: Optional[str] = Field(alias="relayIPAddress",default=None,)
	relayPort: Optional[int] = Field(alias="relayPort",default=None,)
	sentQualityEventRatio: float | str | ReferenceNumeric
	subnet: Optional[str] = Field(alias="subnet",default=None,)
	traceRouteHops: Optional[list[CallRecordsTraceRouteHop]] = Field(alias="traceRouteHops",default=None,)
	wifiBand: Optional[CallRecordsWifiBand | str] = Field(alias="wifiBand",default=None,)
	wifiBatteryCharge: Optional[int] = Field(alias="wifiBatteryCharge",default=None,)
	wifiChannel: Optional[int] = Field(alias="wifiChannel",default=None,)
	wifiMicrosoftDriver: Optional[str] = Field(alias="wifiMicrosoftDriver",default=None,)
	wifiMicrosoftDriverVersion: Optional[str] = Field(alias="wifiMicrosoftDriverVersion",default=None,)
	wifiRadioType: Optional[CallRecordsWifiRadioType | str] = Field(alias="wifiRadioType",default=None,)
	wifiSignalStrength: Optional[int] = Field(alias="wifiSignalStrength",default=None,)
	wifiVendorDriver: Optional[str] = Field(alias="wifiVendorDriver",default=None,)
	wifiVendorDriverVersion: Optional[str] = Field(alias="wifiVendorDriverVersion",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric
from .call_records_network_connection_type import CallRecordsNetworkConnectionType
from .reference_numeric import ReferenceNumeric
from .call_records_network_transport_protocol import CallRecordsNetworkTransportProtocol
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .call_records_trace_route_hop import CallRecordsTraceRouteHop
from .call_records_wifi_band import CallRecordsWifiBand
from .call_records_wifi_radio_type import CallRecordsWifiRadioType

