from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class End_breakPostRequest(BaseModel):
	isAtApprovedLocation: Optional[bool] = Field(alias="isAtApprovedLocation", default=None,)
	notes: Optional[ItemBody] = Field(alias="notes", default=None,)

from .item_body import ItemBody
