from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminAccessDetails(BaseModel):
	unifiedRoles: Optional[list[UnifiedRole]] = Field(default=None,alias="unifiedRoles",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .unified_role import UnifiedRole

