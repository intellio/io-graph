from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsAssociatedIdentities(BaseModel):
	all: SerializeAsAny[Optional[list[AwsIdentity]]] = Field(alias="all",default=None,)
	roles: Optional[list[AwsRole]] = Field(alias="roles",default=None,)
	users: Optional[list[AwsUser]] = Field(alias="users",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .aws_identity import AwsIdentity
from .aws_role import AwsRole
from .aws_user import AwsUser

