from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttendeeAvailability(BaseModel):
	attendee: SerializeAsAny[Optional[AttendeeBase]] = Field(default=None,alias="attendee",)
	availability: Optional[FreeBusyStatus] = Field(default=None,alias="availability",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attendee_base import AttendeeBase
from .free_busy_status import FreeBusyStatus

