from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UnifiedRbacResourceNamespace(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRbacResourceNamespace"] = Field(alias="@odata.type",)
	name: Optional[str] = Field(alias="name", default=None,)
	resourceActions: Optional[list[UnifiedRbacResourceAction]] = Field(alias="resourceActions", default=None,)

from .unified_rbac_resource_action import UnifiedRbacResourceAction
