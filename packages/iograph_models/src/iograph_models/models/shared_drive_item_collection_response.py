from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharedDriveItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SharedDriveItem] = Field(alias="value",)

from .shared_drive_item import SharedDriveItem

