from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttendeeAvailability(BaseModel):
	attendee: SerializeAsAny[Optional[AttendeeBase]] = Field(alias="attendee",default=None,)
	availability: Optional[str | FreeBusyStatus] = Field(alias="availability",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attendee_base import AttendeeBase
from .free_busy_status import FreeBusyStatus

