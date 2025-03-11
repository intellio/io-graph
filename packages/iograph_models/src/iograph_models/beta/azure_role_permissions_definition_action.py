from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureRolePermissionsDefinitionAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	roles: Optional[list[PermissionsDefinitionAzureRole]] = Field(alias="roles",default=None,)

from .permissions_definition_azure_role import PermissionsDefinitionAzureRole

