from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosManagedAppProtection]] = Field(alias="value", default=None,)

from .ios_managed_app_protection import IosManagedAppProtection
