from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class TeleconferenceDeviceVideoQuality(BaseModel):
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
	odata_type: Literal["#microsoft.graph.teleconferenceDeviceVideoQuality"] = Field(alias="@odata.type", default="#microsoft.graph.teleconferenceDeviceVideoQuality")
	averageInboundBitRate: float | str | ReferenceNumeric
	averageInboundFrameRate: float | str | ReferenceNumeric
	averageOutboundBitRate: float | str | ReferenceNumeric
	averageOutboundFrameRate: float | str | ReferenceNumeric

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
			if mapping_key == "#microsoft.graph.teleconferenceDeviceScreenSharingQuality":
				from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality
				return TeleconferenceDeviceScreenSharingQuality.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .reference_numeric import ReferenceNumeric
