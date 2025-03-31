from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharePointOneDriveOptions(BaseModel):
	includeContent: Optional[SearchContent | str] = Field(alias="includeContent", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .search_content import SearchContent
