from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityIpAddressCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityIpAddress] = Field(alias="value",)

from .security_ip_address import SecurityIpAddress

