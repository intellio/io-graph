from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRolePermission(BaseModel):
	allowedResourceActions: Optional[list[str]] = Field(alias="allowedResourceActions", default=None,)
	condition: Optional[str] = Field(alias="condition", default=None,)
	excludedResourceActions: Optional[list[str]] = Field(alias="excludedResourceActions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


