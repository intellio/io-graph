from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalMeetingRegistrantCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ExternalMeetingRegistrant]] = Field(alias="value", default=None,)

from .external_meeting_registrant import ExternalMeetingRegistrant
