from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MentionEvent(BaseModel):
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	speaker: SerializeAsAny[Optional[IdentitySet]] = Field(alias="speaker",default=None,)
	transcriptUtterance: Optional[str] = Field(alias="transcriptUtterance",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

