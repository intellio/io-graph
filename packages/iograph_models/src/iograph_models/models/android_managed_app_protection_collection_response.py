from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AndroidManagedAppProtection]] = Field(default=None,alias="value",)

from .android_managed_app_protection import AndroidManagedAppProtection

