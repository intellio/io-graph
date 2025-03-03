from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChecklistItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ChecklistItem]] = Field(default=None,alias="value",)

from .checklist_item import ChecklistItem

