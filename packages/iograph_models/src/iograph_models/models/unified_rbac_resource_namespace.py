from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRbacResourceNamespace(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	resourceActions: Optional[list[UnifiedRbacResourceAction]] = Field(default=None,alias="resourceActions",)

from .unified_rbac_resource_action import UnifiedRbacResourceAction

