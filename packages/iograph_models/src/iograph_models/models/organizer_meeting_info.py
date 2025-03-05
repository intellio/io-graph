from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OrganizerMeetingInfo(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	organizer: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="organizer",)

from .identity_set import IdentitySet

