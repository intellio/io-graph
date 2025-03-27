from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateRolloutSettings(BaseModel):
	offerEndDateTimeInUTC: Optional[datetime] = Field(alias="offerEndDateTimeInUTC", default=None,)
	offerIntervalInDays: Optional[int] = Field(alias="offerIntervalInDays", default=None,)
	offerStartDateTimeInUTC: Optional[datetime] = Field(alias="offerStartDateTimeInUTC", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


