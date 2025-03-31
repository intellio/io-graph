from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidWorkProfileVpnConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidWorkProfileVpnConfiguration]] = Field(alias="value", default=None,)

from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
