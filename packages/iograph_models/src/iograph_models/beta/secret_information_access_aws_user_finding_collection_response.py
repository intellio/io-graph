from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecretInformationAccessAwsUserFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecretInformationAccessAwsUserFinding]] = Field(alias="value", default=None,)

from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
