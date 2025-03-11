from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsPermissionsDefinition(BaseModel):
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo",default=None,)
	identityInfo: Optional[PermissionsDefinitionAuthorizationSystemIdentity] = Field(alias="identityInfo",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionInfo: SerializeAsAny[Optional[AwsPermissionsDefinitionAction]] = Field(alias="actionInfo",default=None,)

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
from .aws_permissions_definition_action import AwsPermissionsDefinitionAction

