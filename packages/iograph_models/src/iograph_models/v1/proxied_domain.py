from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProxiedDomain(BaseModel):
	ipAddressOrFQDN: Optional[str] = Field(alias="ipAddressOrFQDN", default=None,)
	proxy: Optional[str] = Field(alias="proxy", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

