from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RbacApplicationMultiple(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.rbacApplicationMultiple"] = Field(alias="@odata.type",)
	resourceNamespaces: Optional[list[UnifiedRbacResourceNamespace]] = Field(alias="resourceNamespaces", default=None,)
	roleAssignments: Optional[list[UnifiedRoleAssignmentMultiple]] = Field(alias="roleAssignments", default=None,)
	roleDefinitions: Optional[list[UnifiedRoleDefinition]] = Field(alias="roleDefinitions", default=None,)

from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
from .unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple
from .unified_role_definition import UnifiedRoleDefinition
