from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingCustomerInformation(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	customerId: Optional[str] = Field(alias="customerId",default=None,)
	customQuestionAnswers: Optional[list[BookingQuestionAnswer]] = Field(alias="customQuestionAnswers",default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	location: SerializeAsAny[Optional[Location]] = Field(alias="location",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	phone: Optional[str] = Field(alias="phone",default=None,)
	timeZone: Optional[str] = Field(alias="timeZone",default=None,)

from .booking_question_answer import BookingQuestionAnswer
from .location import Location

