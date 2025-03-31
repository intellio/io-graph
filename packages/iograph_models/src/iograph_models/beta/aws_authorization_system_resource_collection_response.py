from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AwsAuthorizationSystemResourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AwsAuthorizationSystemResource]] = Field(alias="value", default=None,)

from .aws_authorization_system_resource import AwsAuthorizationSystemResource
