from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeCardEvent(BaseModel):
	dateTime: Optional[datetime] = Field(alias="dateTime", default=None,)
	isAtApprovedLocation: Optional[bool] = Field(alias="isAtApprovedLocation", default=None,)
	notes: Optional[ItemBody] = Field(alias="notes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .item_body import ItemBody

