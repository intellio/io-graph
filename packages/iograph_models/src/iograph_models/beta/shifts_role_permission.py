from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ShiftsRolePermission(BaseModel):
	allowedResourceActions: Optional[list[str]] = Field(alias="allowedResourceActions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

