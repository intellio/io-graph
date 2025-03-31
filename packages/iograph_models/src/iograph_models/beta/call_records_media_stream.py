from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsMediaStream(BaseModel):
	audioCodec: Optional[CallRecordsAudioCodec | str] = Field(alias="audioCodec", default=None,)
	averageAudioDegradation: float | str | ReferenceNumeric
	averageAudioNetworkJitter: Optional[str] = Field(alias="averageAudioNetworkJitter", default=None,)
	averageBandwidthEstimate: Optional[int] = Field(alias="averageBandwidthEstimate", default=None,)
	averageFreezeDuration: Optional[str] = Field(alias="averageFreezeDuration", default=None,)
	averageJitter: Optional[str] = Field(alias="averageJitter", default=None,)
	averagePacketLossRate: float | str | ReferenceNumeric
	averageRatioOfConcealedSamples: float | str | ReferenceNumeric
	averageReceivedFrameRate: float | str | ReferenceNumeric
	averageRoundTripTime: Optional[str] = Field(alias="averageRoundTripTime", default=None,)
	averageVideoFrameLossPercentage: float | str | ReferenceNumeric
	averageVideoFrameRate: float | str | ReferenceNumeric
	averageVideoPacketLossRate: float | str | ReferenceNumeric
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	isAudioForwardErrorCorrectionUsed: Optional[bool] = Field(alias="isAudioForwardErrorCorrectionUsed", default=None,)
	lowFrameRateRatio: float | str | ReferenceNumeric
	lowVideoProcessingCapabilityRatio: float | str | ReferenceNumeric
	maxAudioNetworkJitter: Optional[str] = Field(alias="maxAudioNetworkJitter", default=None,)
	maxJitter: Optional[str] = Field(alias="maxJitter", default=None,)
	maxPacketLossRate: float | str | ReferenceNumeric
	maxRatioOfConcealedSamples: float | str | ReferenceNumeric
	maxRoundTripTime: Optional[str] = Field(alias="maxRoundTripTime", default=None,)
	packetUtilization: Optional[int] = Field(alias="packetUtilization", default=None,)
	postForwardErrorCorrectionPacketLossRate: float | str | ReferenceNumeric
	rmsFreezeDuration: Optional[str] = Field(alias="rmsFreezeDuration", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	streamDirection: Optional[CallRecordsMediaStreamDirection | str] = Field(alias="streamDirection", default=None,)
	streamId: Optional[str] = Field(alias="streamId", default=None,)
	videoCodec: Optional[CallRecordsVideoCodec | str] = Field(alias="videoCodec", default=None,)
	wasMediaBypassed: Optional[bool] = Field(alias="wasMediaBypassed", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .call_records_audio_codec import CallRecordsAudioCodec
from .reference_numeric import ReferenceNumeric
from .call_records_media_stream_direction import CallRecordsMediaStreamDirection
from .call_records_video_codec import CallRecordsVideoCodec
