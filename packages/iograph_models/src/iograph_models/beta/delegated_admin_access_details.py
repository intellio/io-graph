from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedAdminAccessDetails(BaseModel):
	unifiedRoles: Optional[list[UnifiedRole]] = Field(alias="unifiedRoles", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .unified_role import UnifiedRole

