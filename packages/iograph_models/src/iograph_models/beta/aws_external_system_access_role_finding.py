from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AwsExternalSystemAccessRoleFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.awsExternalSystemAccessRoleFinding"] = Field(alias="@odata.type", default="#microsoft.graph.awsExternalSystemAccessRoleFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessibleSystemIds: Optional[list[str]] = Field(alias="accessibleSystemIds", default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex", default=None,)
	role: Optional[AwsRole] = Field(alias="role", default=None,)

from .permissions_creep_index import PermissionsCreepIndex
from .aws_role import AwsRole
