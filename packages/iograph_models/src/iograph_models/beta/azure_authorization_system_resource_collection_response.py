from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AzureAuthorizationSystemResourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AzureAuthorizationSystemResource]] = Field(alias="value", default=None,)

from .azure_authorization_system_resource import AzureAuthorizationSystemResource
