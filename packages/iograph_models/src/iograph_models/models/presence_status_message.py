from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PresenceStatusMessage(BaseModel):
	expiryDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="expiryDateTime",)
	message: Optional[ItemBody] = Field(default=None,alias="message",)
	publishedDateTime: Optional[datetime] = Field(default=None,alias="publishedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .date_time_time_zone import DateTimeTimeZone
from .item_body import ItemBody

