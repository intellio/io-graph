from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OrganizerMeetingInfo(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	organizer: SerializeAsAny[Optional[IdentitySet]] = Field(alias="organizer",default=None,)

from .identity_set import IdentitySet

