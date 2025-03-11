from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsDefinitionAuthorizationSystemIdentity(BaseModel):
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	identityType: Optional[PermissionsDefinitionIdentityType | str] = Field(alias="identityType",default=None,)
	source: SerializeAsAny[Optional[PermissionsDefinitionIdentitySource]] = Field(alias="source",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .permissions_definition_identity_type import PermissionsDefinitionIdentityType
from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource

