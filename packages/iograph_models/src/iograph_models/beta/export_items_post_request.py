from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Export_itemsPostRequest(BaseModel):
	ItemIds: Optional[list[str]] = Field(alias="ItemIds", default=None,)

