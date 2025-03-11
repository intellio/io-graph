from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDateDrivenRolloutSettings(BaseModel):
	durationBetweenOffers: Optional[str] = Field(alias="durationBetweenOffers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)


