from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionProxiedDomainCollection(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	proxiedDomains: Optional[list[ProxiedDomain]] = Field(default=None,alias="proxiedDomains",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .proxied_domain import ProxiedDomain

