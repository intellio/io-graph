from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IncomingCallOptions(BaseModel):
	hideBotAfterEscalation: Optional[bool] = Field(default=None,alias="hideBotAfterEscalation",)
	isContentSharingNotificationEnabled: Optional[bool] = Field(default=None,alias="isContentSharingNotificationEnabled",)
	isDeltaRosterEnabled: Optional[bool] = Field(default=None,alias="isDeltaRosterEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


