from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AttendeeAvailability(BaseModel):
	attendee: Optional[Union[Attendee]] = Field(alias="attendee", default=None,discriminator="odata_type", )
	availability: Optional[FreeBusyStatus | str] = Field(alias="availability", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .attendee import Attendee
from .free_busy_status import FreeBusyStatus
