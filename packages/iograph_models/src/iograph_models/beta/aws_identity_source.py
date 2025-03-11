from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsIdentitySource(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo",default=None,)

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem

