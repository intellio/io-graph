from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Clock_outPostRequest(BaseModel):
	isAtApprovedLocation: Optional[bool] = Field(default=None,alias="isAtApprovedLocation",)
	notes: Optional[ItemBody] = Field(default=None,alias="notes",)

from .item_body import ItemBody

