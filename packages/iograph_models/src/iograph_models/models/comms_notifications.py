from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommsNotifications(BaseModel):
	value: Optional[list[CommsNotification]] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .comms_notification import CommsNotification

