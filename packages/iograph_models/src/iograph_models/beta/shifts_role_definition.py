from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ShiftsRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.shiftsRoleDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.shiftsRoleDefinition")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	shiftsRolePermissions: Optional[list[ShiftsRolePermission]] = Field(alias="shiftsRolePermissions", default=None,)

from .shifts_role_permission import ShiftsRolePermission
