from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	isElevated: Optional[bool] = Field(alias="isElevated", default=None,)
	resultMessage: Optional[str] = Field(alias="resultMessage", default=None,)
	roleId: Optional[str] = Field(alias="roleId", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	roleInfo: Optional[PrivilegedRole] = Field(alias="roleInfo", default=None,)

from .privileged_role import PrivilegedRole

