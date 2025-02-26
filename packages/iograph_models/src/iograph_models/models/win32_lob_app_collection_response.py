from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Win32LobApp] = Field(alias="value",)

from .win32_lob_app import Win32LobApp

