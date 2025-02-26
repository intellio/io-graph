from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeleconferenceDeviceScreenSharingQuality(BaseModel):
	averageInboundJitter: Optional[str] = Field(default=None,alias="averageInboundJitter",)
	averageInboundPacketLossRateInPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	averageInboundRoundTripDelay: Optional[str] = Field(default=None,alias="averageInboundRoundTripDelay",)
	averageOutboundJitter: Optional[str] = Field(default=None,alias="averageOutboundJitter",)
	averageOutboundPacketLossRateInPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	averageOutboundRoundTripDelay: Optional[str] = Field(default=None,alias="averageOutboundRoundTripDelay",)
	channelIndex: Optional[int] = Field(default=None,alias="channelIndex",)
	inboundPackets: Optional[int] = Field(default=None,alias="inboundPackets",)
	localIPAddress: Optional[str] = Field(default=None,alias="localIPAddress",)
	localPort: Optional[int] = Field(default=None,alias="localPort",)
	maximumInboundJitter: Optional[str] = Field(default=None,alias="maximumInboundJitter",)
	maximumInboundPacketLossRateInPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	maximumInboundRoundTripDelay: Optional[str] = Field(default=None,alias="maximumInboundRoundTripDelay",)
	maximumOutboundJitter: Optional[str] = Field(default=None,alias="maximumOutboundJitter",)
	maximumOutboundPacketLossRateInPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	maximumOutboundRoundTripDelay: Optional[str] = Field(default=None,alias="maximumOutboundRoundTripDelay",)
	mediaDuration: Optional[str] = Field(default=None,alias="mediaDuration",)
	networkLinkSpeedInBytes: Optional[int] = Field(default=None,alias="networkLinkSpeedInBytes",)
	outboundPackets: Optional[int] = Field(default=None,alias="outboundPackets",)
	remoteIPAddress: Optional[str] = Field(default=None,alias="remoteIPAddress",)
	remotePort: Optional[int] = Field(default=None,alias="remotePort",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	averageInboundBitRate: Optional[float] | Optional[str] | ReferenceNumeric
	averageInboundFrameRate: Optional[float] | Optional[str] | ReferenceNumeric
	averageOutboundBitRate: Optional[float] | Optional[str] | ReferenceNumeric
	averageOutboundFrameRate: Optional[float] | Optional[str] | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

