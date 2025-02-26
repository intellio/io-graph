from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosManagedAppProtection] = Field(alias="value",)

from .ios_managed_app_protection import IosManagedAppProtection

