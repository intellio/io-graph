from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosBookmark(BaseModel):
	bookmarkFolder: Optional[str] = Field(alias="bookmarkFolder", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

