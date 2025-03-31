from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsMyRole(BaseModel):
	assignments: Optional[list[ManagedTenantsRoleAssignment]] = Field(alias="assignments", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_role_assignment import ManagedTenantsRoleAssignment
