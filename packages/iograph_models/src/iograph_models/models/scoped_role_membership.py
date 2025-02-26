from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ScopedRoleMembership(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	administrativeUnitId: Optional[str] = Field(default=None,alias="administrativeUnitId",)
	roleId: Optional[str] = Field(default=None,alias="roleId",)
	roleMemberInfo: Optional[Identity] = Field(default=None,alias="roleMemberInfo",)

from .identity import Identity

