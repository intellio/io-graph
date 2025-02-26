from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedAppProtection] = Field(alias="value",)

from .managed_app_protection import ManagedAppProtection

