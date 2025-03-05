from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EntitlementManagementSchedule(BaseModel):
	expiration: Optional[ExpirationPattern] = Field(default=None,alias="expiration",)
	recurrence: Optional[PatternedRecurrence] = Field(default=None,alias="recurrence",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .expiration_pattern import ExpirationPattern
from .patterned_recurrence import PatternedRecurrence

