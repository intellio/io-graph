from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class SingleResourceGcpPermissionsDefinition(BaseModel):
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo", default=None,)
	identityInfo: Optional[PermissionsDefinitionAuthorizationSystemIdentity] = Field(alias="identityInfo", default=None,)
	odata_type: Literal["#microsoft.graph.singleResourceGcpPermissionsDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.singleResourceGcpPermissionsDefinition")
	actionInfo: Optional[Union[GcpActionPermissionsDefinitionAction, GcpRolePermissionsDefinitionAction]] = Field(alias="actionInfo", default=None,discriminator="odata_type", )
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction
