from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RolePermission(BaseModel):
	actions: Optional[list[str]] = Field(alias="actions", default=None,)
	resourceActions: Optional[list[ResourceAction]] = Field(alias="resourceActions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .resource_action import ResourceAction
