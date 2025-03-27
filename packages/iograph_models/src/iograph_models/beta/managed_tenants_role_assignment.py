from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsRoleAssignment(BaseModel):
	assignmentType: Optional[ManagedTenantsDelegatedPrivilegeStatus | str] = Field(alias="assignmentType", default=None,)
	roles: Optional[list[ManagedTenantsRoleDefinition]] = Field(alias="roles", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_delegated_privilege_status import ManagedTenantsDelegatedPrivilegeStatus
from .managed_tenants_role_definition import ManagedTenantsRoleDefinition

