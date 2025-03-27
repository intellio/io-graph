from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecretInformationAccessAwsRoleFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecretInformationAccessAwsRoleFinding]] = Field(alias="value", default=None,)

from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding

