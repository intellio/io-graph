from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppRestartSettings(BaseModel):
	countdownDisplayBeforeRestartInMinutes: Optional[int] = Field(default=None,alias="countdownDisplayBeforeRestartInMinutes",)
	gracePeriodInMinutes: Optional[int] = Field(default=None,alias="gracePeriodInMinutes",)
	restartNotificationSnoozeDurationInMinutes: Optional[int] = Field(default=None,alias="restartNotificationSnoozeDurationInMinutes",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


