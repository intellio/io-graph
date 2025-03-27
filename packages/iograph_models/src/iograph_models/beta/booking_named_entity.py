from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class BookingNamedEntity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

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
			if mapping_key == "#microsoft.graph.bookingBusiness":
				from .booking_business import BookingBusiness
				return BookingBusiness.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingPerson":
				from .booking_person import BookingPerson
				return BookingPerson.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCustomer":
				from .booking_customer import BookingCustomer
				return BookingCustomer.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingStaffMember":
				from .booking_staff_member import BookingStaffMember
				return BookingStaffMember.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingService":
				from .booking_service import BookingService
				return BookingService.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


