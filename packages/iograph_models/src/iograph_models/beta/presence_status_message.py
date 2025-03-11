from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PresenceStatusMessage(BaseModel):
	expiryDateTime: Optional[DateTimeTimeZone] = Field(alias="expiryDateTime",default=None,)
	message: Optional[ItemBody] = Field(alias="message",default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .date_time_time_zone import DateTimeTimeZone
from .item_body import ItemBody

