from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewHistoryScheduleSettings(BaseModel):
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence",default=None,)
	reportRange: Optional[str] = Field(alias="reportRange",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .patterned_recurrence import PatternedRecurrence

