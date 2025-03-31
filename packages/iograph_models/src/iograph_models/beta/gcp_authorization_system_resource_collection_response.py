from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GcpAuthorizationSystemResourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GcpAuthorizationSystemResource]] = Field(alias="value", default=None,)

from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
