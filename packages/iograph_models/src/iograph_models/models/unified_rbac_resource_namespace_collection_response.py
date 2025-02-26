from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRbacResourceNamespaceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UnifiedRbacResourceNamespace] = Field(alias="value",)

from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace

