from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SuggestedEnrollmentLimit(BaseModel):
	suggestedDailyLimit: Optional[int] = Field(alias="suggestedDailyLimit", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


