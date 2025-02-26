from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OrganizerMeetingInfo(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	organizer: Optional[IdentitySet] = Field(default=None,alias="organizer",)

from .identity_set import IdentitySet

