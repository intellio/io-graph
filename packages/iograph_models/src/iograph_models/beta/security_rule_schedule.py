from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRuleSchedule(BaseModel):
	nextRunDateTime: Optional[datetime] = Field(alias="nextRunDateTime", default=None,)
	period: Optional[str] = Field(alias="period", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


