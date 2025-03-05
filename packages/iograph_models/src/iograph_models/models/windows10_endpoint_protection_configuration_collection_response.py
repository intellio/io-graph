from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10EndpointProtectionConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[Windows10EndpointProtectionConfiguration]] = Field(default=None,alias="value",)

from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration

