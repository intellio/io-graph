from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class StandardTimeZoneOffset(BaseModel):
	dayOccurrence: Optional[int] = Field(default=None,alias="dayOccurrence",)
	dayOfWeek: Optional[DayOfWeek] = Field(default=None,alias="dayOfWeek",)
	month: Optional[int] = Field(default=None,alias="month",)
	time: Optional[str] = Field(default=None,alias="time",)
	year: Optional[int] = Field(default=None,alias="year",)
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
			if mapping_key == "#microsoft.graph.daylightTimeZoneOffset":
				from .daylight_time_zone_offset import DaylightTimeZoneOffset
				return DaylightTimeZoneOffset.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .day_of_week import DayOfWeek

