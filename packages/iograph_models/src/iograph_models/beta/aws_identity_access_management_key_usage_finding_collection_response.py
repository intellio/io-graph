from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsIdentityAccessManagementKeyUsageFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AwsIdentityAccessManagementKeyUsageFinding]] = Field(alias="value", default=None,)

from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding

