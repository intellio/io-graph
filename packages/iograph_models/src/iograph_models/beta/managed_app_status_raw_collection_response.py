from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppStatusRawCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedAppStatusRaw]] = Field(alias="value", default=None,)

from .managed_app_status_raw import ManagedAppStatusRaw
