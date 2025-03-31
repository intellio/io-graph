from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GcpRolePermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.gcpRolePermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.gcpRolePermissionsDefinitionAction")
	roles: Optional[list[PermissionsDefinitionGcpRole]] = Field(alias="roles", default=None,)

from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole
