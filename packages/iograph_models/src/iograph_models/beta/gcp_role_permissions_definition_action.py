from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GcpRolePermissionsDefinitionAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	roles: Optional[list[PermissionsDefinitionGcpRole]] = Field(alias="roles",default=None,)

from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole

