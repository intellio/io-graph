from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class Reminder(BaseModel):
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	eventEndTime: Optional[DateTimeTimeZone] = Field(alias="eventEndTime", default=None,)
	eventId: Optional[str] = Field(alias="eventId", default=None,)
	eventLocation: Optional[Union[LocationConstraintItem]] = Field(alias="eventLocation", default=None,discriminator="odata_type", )
	eventStartTime: Optional[DateTimeTimeZone] = Field(alias="eventStartTime", default=None,)
	eventSubject: Optional[str] = Field(alias="eventSubject", default=None,)
	eventWebLink: Optional[str] = Field(alias="eventWebLink", default=None,)
	reminderFireTime: Optional[DateTimeTimeZone] = Field(alias="reminderFireTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .date_time_time_zone import DateTimeTimeZone
from .location_constraint_item import LocationConstraintItem
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

