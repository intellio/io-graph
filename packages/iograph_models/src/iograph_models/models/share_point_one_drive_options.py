from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharePointOneDriveOptions(BaseModel):
	includeContent: Optional[SearchContent] = Field(default=None,alias="includeContent",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_content import SearchContent

