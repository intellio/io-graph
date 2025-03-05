from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeleconferenceDeviceAudioQuality(BaseModel):
	averageInboundJitter: Optional[str] = Field(default=None,alias="averageInboundJitter",)
	averageInboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	averageInboundRoundTripDelay: Optional[str] = Field(default=None,alias="averageInboundRoundTripDelay",)
	averageOutboundJitter: Optional[str] = Field(default=None,alias="averageOutboundJitter",)
	averageOutboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	averageOutboundRoundTripDelay: Optional[str] = Field(default=None,alias="averageOutboundRoundTripDelay",)
	channelIndex: Optional[int] = Field(default=None,alias="channelIndex",)
	inboundPackets: Optional[int] = Field(default=None,alias="inboundPackets",)
	localIPAddress: Optional[str] = Field(default=None,alias="localIPAddress",)
	localPort: Optional[int] = Field(default=None,alias="localPort",)
	maximumInboundJitter: Optional[str] = Field(default=None,alias="maximumInboundJitter",)
	maximumInboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	maximumInboundRoundTripDelay: Optional[str] = Field(default=None,alias="maximumInboundRoundTripDelay",)
	maximumOutboundJitter: Optional[str] = Field(default=None,alias="maximumOutboundJitter",)
	maximumOutboundPacketLossRateInPercentage: float | str | ReferenceNumeric
	maximumOutboundRoundTripDelay: Optional[str] = Field(default=None,alias="maximumOutboundRoundTripDelay",)
	mediaDuration: Optional[str] = Field(default=None,alias="mediaDuration",)
	networkLinkSpeedInBytes: Optional[int] = Field(default=None,alias="networkLinkSpeedInBytes",)
	outboundPackets: Optional[int] = Field(default=None,alias="outboundPackets",)
	remoteIPAddress: Optional[str] = Field(default=None,alias="remoteIPAddress",)
	remotePort: Optional[int] = Field(default=None,alias="remotePort",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

