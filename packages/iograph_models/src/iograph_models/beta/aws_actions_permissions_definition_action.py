from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AwsActionsPermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.awsActionsPermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.awsActionsPermissionsDefinitionAction")
	assignToRoleId: Optional[str] = Field(alias="assignToRoleId", default=None,)
	statements: Optional[list[AwsStatement]] = Field(alias="statements", default=None,)

from .aws_statement import AwsStatement
