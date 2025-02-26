from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppStatusRawCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedAppStatusRaw] = Field(alias="value",)

from .managed_app_status_raw import ManagedAppStatusRaw

