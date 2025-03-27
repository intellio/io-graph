from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRbacResourceNamespace(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	resourceActions: Optional[list[UnifiedRbacResourceAction]] = Field(alias="resourceActions", default=None,)

from .unified_rbac_resource_action import UnifiedRbacResourceAction

