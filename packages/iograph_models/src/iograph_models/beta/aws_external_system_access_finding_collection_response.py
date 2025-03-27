from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsExternalSystemAccessFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AwsExternalSystemAccessFinding]] = Field(alias="value", default=None,)

from .aws_external_system_access_finding import AwsExternalSystemAccessFinding

