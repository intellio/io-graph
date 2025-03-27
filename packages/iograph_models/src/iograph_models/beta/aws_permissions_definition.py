from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AwsPermissionsDefinition(BaseModel):
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo", default=None,)
	identityInfo: Optional[PermissionsDefinitionAuthorizationSystemIdentity] = Field(alias="identityInfo", default=None,)
	odata_type: Literal["#microsoft.graph.awsPermissionsDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.awsPermissionsDefinition")
	actionInfo: Optional[Union[AwsActionsPermissionsDefinitionAction, AwsPolicyPermissionsDefinitionAction]] = Field(alias="actionInfo", default=None,discriminator="odata_type", )

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
from .aws_actions_permissions_definition_action import AwsActionsPermissionsDefinitionAction
from .aws_policy_permissions_definition_action import AwsPolicyPermissionsDefinitionAction

