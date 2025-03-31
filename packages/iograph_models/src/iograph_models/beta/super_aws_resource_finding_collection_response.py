from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SuperAwsResourceFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SuperAwsResourceFinding]] = Field(alias="value", default=None,)

from .super_aws_resource_finding import SuperAwsResourceFinding
