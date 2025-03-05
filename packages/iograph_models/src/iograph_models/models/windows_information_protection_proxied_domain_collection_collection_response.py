from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionProxiedDomainCollectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WindowsInformationProtectionProxiedDomainCollection]] = Field(default=None,alias="value",)

from .windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection

