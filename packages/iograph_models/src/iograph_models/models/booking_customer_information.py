from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingCustomerInformation(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	customerId: Optional[str] = Field(default=None,alias="customerId",)
	customQuestionAnswers: Optional[list[BookingQuestionAnswer]] = Field(default=None,alias="customQuestionAnswers",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	location: SerializeAsAny[Optional[Location]] = Field(default=None,alias="location",)
	name: Optional[str] = Field(default=None,alias="name",)
	notes: Optional[str] = Field(default=None,alias="notes",)
	phone: Optional[str] = Field(default=None,alias="phone",)
	timeZone: Optional[str] = Field(default=None,alias="timeZone",)

from .booking_question_answer import BookingQuestionAnswer
from .location import Location

