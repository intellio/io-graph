from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EnrollmentTroubleshootingEventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EnrollmentTroubleshootingEvent]] = Field(alias="value", default=None,)

from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
