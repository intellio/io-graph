from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRole(BaseModel):
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

