from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsSecretInformationAccessFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AwsSecretInformationAccessFinding]]] = Field(alias="value",default=None,)

from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding

