from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class BookingCustomerInformation(BaseModel):
	odata_type: Literal["#microsoft.graph.bookingCustomerInformation"] = Field(alias="@odata.type", default="#microsoft.graph.bookingCustomerInformation")
	customerId: Optional[str] = Field(alias="customerId", default=None,)
	customQuestionAnswers: Optional[list[BookingQuestionAnswer]] = Field(alias="customQuestionAnswers", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	location: Optional[Union[LocationConstraintItem]] = Field(alias="location", default=None,discriminator="odata_type", )
	name: Optional[str] = Field(alias="name", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	phone: Optional[str] = Field(alias="phone", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)

from .booking_question_answer import BookingQuestionAnswer
from .location_constraint_item import LocationConstraintItem

