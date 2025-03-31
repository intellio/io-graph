from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosikEv2VpnConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosikEv2VpnConfiguration]] = Field(alias="value", default=None,)

from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
