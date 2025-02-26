from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRolePermission(BaseModel):
	allowedResourceActions: list[str] = Field(alias="allowedResourceActions",)
	condition: Optional[str] = Field(default=None,alias="condition",)
	excludedResourceActions: list[Optional[str]] = Field(alias="excludedResourceActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


