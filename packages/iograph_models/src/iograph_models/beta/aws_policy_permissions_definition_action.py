from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsPolicyPermissionsDefinitionAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignToRoleId: Optional[str] = Field(alias="assignToRoleId",default=None,)
	policies: Optional[list[PermissionsDefinitionAwsPolicy]] = Field(alias="policies",default=None,)

from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy

