from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProxiedDomain(BaseModel):
	ipAddressOrFQDN: Optional[str] = Field(default=None,alias="ipAddressOrFQDN",)
	proxy: Optional[str] = Field(default=None,alias="proxy",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


