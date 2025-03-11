from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityToolAwsUserAdministratorFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityToolAwsUserAdministratorFinding]] = Field(alias="value",default=None,)

from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

