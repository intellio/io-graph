from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionProxiedDomainCollection(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	proxiedDomains: Optional[list[ProxiedDomain]] = Field(alias="proxiedDomains", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .proxied_domain import ProxiedDomain
