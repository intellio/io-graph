from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityToolAwsServerlessFunctionAdministratorFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityToolAwsServerlessFunctionAdministratorFinding]] = Field(alias="value", default=None,)

from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
