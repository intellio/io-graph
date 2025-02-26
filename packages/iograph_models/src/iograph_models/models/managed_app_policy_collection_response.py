from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedAppPolicy] = Field(alias="value",)

from .managed_app_policy import ManagedAppPolicy

