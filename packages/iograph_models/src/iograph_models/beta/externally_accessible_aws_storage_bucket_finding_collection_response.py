from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternallyAccessibleAwsStorageBucketFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ExternallyAccessibleAwsStorageBucketFinding]] = Field(alias="value", default=None,)

from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding

