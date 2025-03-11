from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ScopedRoleMembership(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	administrativeUnitId: Optional[str] = Field(alias="administrativeUnitId",default=None,)
	roleId: Optional[str] = Field(alias="roleId",default=None,)
	roleMemberInfo: SerializeAsAny[Optional[Identity]] = Field(alias="roleMemberInfo",default=None,)

from .identity import Identity

