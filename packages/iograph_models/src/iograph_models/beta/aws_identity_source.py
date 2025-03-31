from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AwsIdentitySource(BaseModel):
	odata_type: Literal["#microsoft.graph.awsIdentitySource"] = Field(alias="@odata.type", default="#microsoft.graph.awsIdentitySource")
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo", default=None,)

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
