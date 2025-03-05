from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRbacResourceNamespaceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[UnifiedRbacResourceNamespace]] = Field(alias="value",default=None,)

from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace

