from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RolePermission(BaseModel):
	resourceActions: Optional[list[ResourceAction]] = Field(default=None,alias="resourceActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .resource_action import ResourceAction

