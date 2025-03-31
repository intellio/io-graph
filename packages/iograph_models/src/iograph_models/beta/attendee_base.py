from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AttendeeBase(BaseModel):
	emailAddress: Optional[Union[TypedEmailAddress]] = Field(alias="emailAddress", default=None,discriminator="odata_type", )
	odata_type: Literal["#microsoft.graph.attendeeBase"] = Field(alias="@odata.type", default="#microsoft.graph.attendeeBase")
	type: Optional[AttendeeType | str] = Field(alias="type", default=None,)

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
			if mapping_key == "#microsoft.graph.attendee":
				from .attendee import Attendee
				return Attendee.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .typed_email_address import TypedEmailAddress
from .attendee_type import AttendeeType
