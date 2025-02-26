from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidLobAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AndroidLobApp] = Field(alias="value",)

from .android_lob_app import AndroidLobApp

