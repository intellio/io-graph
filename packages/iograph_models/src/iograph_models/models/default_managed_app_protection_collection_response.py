from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DefaultManagedAppProtection] = Field(alias="value",)

from .default_managed_app_protection import DefaultManagedAppProtection

