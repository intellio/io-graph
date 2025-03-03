from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAndroidLobAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ManagedAndroidLobApp]] = Field(default=None,alias="value",)

from .managed_android_lob_app import ManagedAndroidLobApp

