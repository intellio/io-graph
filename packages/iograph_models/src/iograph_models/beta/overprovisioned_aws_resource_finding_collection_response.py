from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OverprovisionedAwsResourceFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[OverprovisionedAwsResourceFinding]] = Field(alias="value",default=None,)

from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding

