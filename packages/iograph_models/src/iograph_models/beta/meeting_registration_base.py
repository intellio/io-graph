from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingRegistrationBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedRegistrant: Optional[MeetingAudience | str] = Field(alias="allowedRegistrant",default=None,)
	registrants: SerializeAsAny[Optional[list[MeetingRegistrantBase]]] = Field(alias="registrants",default=None,)

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
			if mapping_key == "#microsoft.graph.externalMeetingRegistration":
				from .external_meeting_registration import ExternalMeetingRegistration
				return ExternalMeetingRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingRegistration":
				from .meeting_registration import MeetingRegistration
				return MeetingRegistration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .meeting_audience import MeetingAudience
from .meeting_registrant_base import MeetingRegistrantBase

