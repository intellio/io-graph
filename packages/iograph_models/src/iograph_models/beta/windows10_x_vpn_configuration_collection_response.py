from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10XVpnConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10XVpnConfiguration]] = Field(alias="value", default=None,)

from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
