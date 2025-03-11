from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppRestartSettings(BaseModel):
	countdownDisplayBeforeRestartInMinutes: Optional[int] = Field(alias="countdownDisplayBeforeRestartInMinutes",default=None,)
	gracePeriodInMinutes: Optional[int] = Field(alias="gracePeriodInMinutes",default=None,)
	restartNotificationSnoozeDurationInMinutes: Optional[int] = Field(alias="restartNotificationSnoozeDurationInMinutes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


