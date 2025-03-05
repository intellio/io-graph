from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewHistoryScheduleSettings(BaseModel):
	recurrence: Optional[PatternedRecurrence] = Field(default=None,alias="recurrence",)
	reportRange: Optional[str] = Field(default=None,alias="reportRange",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .patterned_recurrence import PatternedRecurrence

