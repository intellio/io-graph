from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[Win32LobAppRule]] = Field(default=None,alias="value",)

from .win32_lob_app_rule import Win32LobAppRule

