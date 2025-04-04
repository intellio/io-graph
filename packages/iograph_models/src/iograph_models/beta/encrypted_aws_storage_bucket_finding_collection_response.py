from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EncryptedAwsStorageBucketFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EncryptedAwsStorageBucketFinding]] = Field(alias="value", default=None,)

from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
