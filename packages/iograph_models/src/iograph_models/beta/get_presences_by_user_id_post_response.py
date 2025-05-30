from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_presences_by_user_idPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Presence]] = Field(alias="value", default=None,)

from .presence import Presence
