from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TimeCardEvent(BaseModel):
	dateTime: Optional[datetime] = Field(default=None,alias="dateTime",)
	isAtApprovedLocation: Optional[bool] = Field(default=None,alias="isAtApprovedLocation",)
	notes: Optional[ItemBody] = Field(default=None,alias="notes",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .item_body import ItemBody

