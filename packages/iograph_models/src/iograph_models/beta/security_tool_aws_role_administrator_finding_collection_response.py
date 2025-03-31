from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityToolAwsRoleAdministratorFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityToolAwsRoleAdministratorFinding]] = Field(alias="value", default=None,)

from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
