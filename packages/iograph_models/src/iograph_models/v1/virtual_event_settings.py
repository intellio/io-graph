from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventSettings(BaseModel):
	isAttendeeEmailNotificationEnabled: Optional[bool] = Field(alias="isAttendeeEmailNotificationEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


