from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AwsSecurityToolAdministrationFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecurityToolAwsResourceAdministratorFinding, SecurityToolAwsRoleAdministratorFinding, SecurityToolAwsServerlessFunctionAdministratorFinding, SecurityToolAwsUserAdministratorFinding],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

