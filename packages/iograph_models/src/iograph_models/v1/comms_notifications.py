from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommsNotifications(BaseModel):
	value: Optional[list[CommsNotification]] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .comms_notification import CommsNotification

