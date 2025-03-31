from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintServiceEndpointCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PrintServiceEndpoint]] = Field(alias="value", default=None,)

from .print_service_endpoint import PrintServiceEndpoint
