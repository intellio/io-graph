from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsActionsPermissionsDefinitionAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignToRoleId: Optional[str] = Field(alias="assignToRoleId",default=None,)
	statements: Optional[list[AwsStatement]] = Field(alias="statements",default=None,)

from .aws_statement import AwsStatement

