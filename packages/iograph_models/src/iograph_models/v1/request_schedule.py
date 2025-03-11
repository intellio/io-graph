from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RequestSchedule(BaseModel):
	expiration: Optional[ExpirationPattern] = Field(alias="expiration",default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .expiration_pattern import ExpirationPattern
from .patterned_recurrence import PatternedRecurrence

