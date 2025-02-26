from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EnrollmentTroubleshootingEventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EnrollmentTroubleshootingEvent] = Field(alias="value",)

from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent

