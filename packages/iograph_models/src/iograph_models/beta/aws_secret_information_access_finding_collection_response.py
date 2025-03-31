from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AwsSecretInformationAccessFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecretInformationAccessAwsResourceFinding, SecretInformationAccessAwsRoleFinding, SecretInformationAccessAwsServerlessFunctionFinding, SecretInformationAccessAwsUserFinding],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
