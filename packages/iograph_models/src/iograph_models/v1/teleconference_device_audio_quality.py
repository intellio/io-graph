from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TeleconferenceDeviceAudioQuality(BaseModel):
	averageInboundJitter: Optional[str] = Field(alias="averageInboundJitter", default=None,)
	averageInboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	averageInboundRoundTripDelay: Optional[str] = Field(alias="averageInboundRoundTripDelay", default=None,)
	averageOutboundJitter: Optional[str] = Field(alias="averageOutboundJitter", default=None,)
	averageOutboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	averageOutboundRoundTripDelay: Optional[str] = Field(alias="averageOutboundRoundTripDelay", default=None,)
	channelIndex: Optional[int] = Field(alias="channelIndex", default=None,)
	inboundPackets: Optional[int] = Field(alias="inboundPackets", default=None,)
	localIPAddress: Optional[str] = Field(alias="localIPAddress", default=None,)
	localPort: Optional[int] = Field(alias="localPort", default=None,)
	maximumInboundJitter: Optional[str] = Field(alias="maximumInboundJitter", default=None,)
	maximumInboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	maximumInboundRoundTripDelay: Optional[str] = Field(alias="maximumInboundRoundTripDelay", default=None,)
	maximumOutboundJitter: Optional[str] = Field(alias="maximumOutboundJitter", default=None,)
	maximumOutboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	maximumOutboundRoundTripDelay: Optional[str] = Field(alias="maximumOutboundRoundTripDelay", default=None,)
	mediaDuration: Optional[str] = Field(alias="mediaDuration", default=None,)
	networkLinkSpeedInBytes: Optional[int] = Field(alias="networkLinkSpeedInBytes", default=None,)
	outboundPackets: Optional[int] = Field(alias="outboundPackets", default=None,)
	remoteIPAddress: Optional[str] = Field(alias="remoteIPAddress", default=None,)
	remotePort: Optional[int] = Field(alias="remotePort", default=None,)
	odata_type: Literal["#microsoft.graph.teleconferenceDeviceAudioQuality"] = Field(alias="@odata.type", default="#microsoft.graph.teleconferenceDeviceAudioQuality")

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

