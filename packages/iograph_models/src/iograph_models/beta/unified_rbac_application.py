from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRbacApplication(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	customAppScopes: Optional[list[CustomAppScope]] = Field(alias="customAppScopes",default=None,)
	resourceNamespaces: Optional[list[UnifiedRbacResourceNamespace]] = Field(alias="resourceNamespaces",default=None,)
	roleAssignments: Optional[list[UnifiedRoleAssignment]] = Field(alias="roleAssignments",default=None,)
	roleDefinitions: Optional[list[UnifiedRoleDefinition]] = Field(alias="roleDefinitions",default=None,)
	transitiveRoleAssignments: Optional[list[UnifiedRoleAssignment]] = Field(alias="transitiveRoleAssignments",default=None,)

from .custom_app_scope import CustomAppScope
from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
from .unified_role_assignment import UnifiedRoleAssignment
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_assignment import UnifiedRoleAssignment

