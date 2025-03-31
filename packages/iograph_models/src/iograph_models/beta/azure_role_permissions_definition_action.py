from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AzureRolePermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.azureRolePermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.azureRolePermissionsDefinitionAction")
	roles: Optional[list[PermissionsDefinitionAzureRole]] = Field(alias="roles", default=None,)

from .permissions_definition_azure_role import PermissionsDefinitionAzureRole
