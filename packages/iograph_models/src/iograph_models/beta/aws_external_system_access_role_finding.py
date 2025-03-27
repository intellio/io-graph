from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AwsExternalSystemAccessRoleFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessibleSystemIds: Optional[list[str]] = Field(alias="accessibleSystemIds", default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex", default=None,)
	role: Optional[AwsRole] = Field(alias="role", default=None,)

from .permissions_creep_index import PermissionsCreepIndex
from .aws_role import AwsRole

