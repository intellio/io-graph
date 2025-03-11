from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsRole(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	source: SerializeAsAny[Optional[AuthorizationSystemIdentitySource]] = Field(alias="source",default=None,)
	authorizationSystem: SerializeAsAny[Optional[AuthorizationSystem]] = Field(alias="authorizationSystem",default=None,)
	roleType: Optional[AwsRoleType | str] = Field(alias="roleType",default=None,)
	trustEntityType: Optional[AwsRoleTrustEntityType | str] = Field(alias="trustEntityType",default=None,)

from .authorization_system_identity_source import AuthorizationSystemIdentitySource
from .authorization_system import AuthorizationSystem
from .aws_role_type import AwsRoleType
from .aws_role_trust_entity_type import AwsRoleTrustEntityType

