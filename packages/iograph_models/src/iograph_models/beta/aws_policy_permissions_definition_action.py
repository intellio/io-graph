from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AwsPolicyPermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.awsPolicyPermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.awsPolicyPermissionsDefinitionAction")
	assignToRoleId: Optional[str] = Field(alias="assignToRoleId", default=None,)
	policies: Optional[list[PermissionsDefinitionAwsPolicy]] = Field(alias="policies", default=None,)

from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy

