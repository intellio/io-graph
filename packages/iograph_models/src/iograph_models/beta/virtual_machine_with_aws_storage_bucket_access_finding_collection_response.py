from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualMachineWithAwsStorageBucketAccessFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VirtualMachineWithAwsStorageBucketAccessFinding]] = Field(alias="value", default=None,)

from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding

