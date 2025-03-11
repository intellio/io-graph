from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewRecurrenceSettings(BaseModel):
	durationInDays: Optional[int] = Field(alias="durationInDays",default=None,)
	recurrenceCount: Optional[int] = Field(alias="recurrenceCount",default=None,)
	recurrenceEndType: Optional[str] = Field(alias="recurrenceEndType",default=None,)
	recurrenceType: Optional[str] = Field(alias="recurrenceType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


