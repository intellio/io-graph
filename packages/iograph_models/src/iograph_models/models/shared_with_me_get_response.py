from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Shared_with_meGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DriveItem]] = Field(default=None,alias="value",)

from .drive_item import DriveItem

