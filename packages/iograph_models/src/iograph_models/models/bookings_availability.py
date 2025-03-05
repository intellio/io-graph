from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class BookingsAvailability(BaseModel):
	availabilityType: Optional[BookingsServiceAvailabilityType] = Field(default=None,alias="availabilityType",)
	businessHours: Optional[list[BookingWorkHours]] = Field(default=None,alias="businessHours",)
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
			if mapping_key == "#microsoft.graph.bookingsAvailabilityWindow":
				from .bookings_availability_window import BookingsAvailabilityWindow
				return BookingsAvailabilityWindow.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .bookings_service_availability_type import BookingsServiceAvailabilityType
from .booking_work_hours import BookingWorkHours

