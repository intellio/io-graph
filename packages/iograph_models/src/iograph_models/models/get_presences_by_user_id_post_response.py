from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_presences_by_user_idPostResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Presence] = Field(alias="value",)

from .presence import Presence

