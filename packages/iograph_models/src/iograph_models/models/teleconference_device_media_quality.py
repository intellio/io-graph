from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class TeleconferenceDeviceMediaQuality(BaseModel):
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

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.teleconferenceDeviceAudioQuality":
				from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality
				return TeleconferenceDeviceAudioQuality.model_validate(data)
			if mapping_key == "#microsoft.graph.teleconferenceDeviceVideoQuality":
				from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality
				return TeleconferenceDeviceVideoQuality.model_validate(data)
			if mapping_key == "#microsoft.graph.teleconferenceDeviceScreenSharingQuality":
				from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality
				return TeleconferenceDeviceScreenSharingQuality.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

