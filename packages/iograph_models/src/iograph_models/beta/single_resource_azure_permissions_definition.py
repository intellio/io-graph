from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SingleResourceAzurePermissionsDefinition(BaseModel):
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo",default=None,)
	identityInfo: Optional[PermissionsDefinitionAuthorizationSystemIdentity] = Field(alias="identityInfo",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionInfo: SerializeAsAny[Optional[AzurePermissionsDefinitionAction]] = Field(alias="actionInfo",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
from .azure_permissions_definition_action import AzurePermissionsDefinitionAction

