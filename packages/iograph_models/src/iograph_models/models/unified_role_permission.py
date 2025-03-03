from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRolePermission(BaseModel):
	allowedResourceActions: Optional[list[str]] = Field(default=None,alias="allowedResourceActions",)
	condition: Optional[str] = Field(default=None,alias="condition",)
	excludedResourceActions: Optional[list[str]] = Field(default=None,alias="excludedResourceActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


