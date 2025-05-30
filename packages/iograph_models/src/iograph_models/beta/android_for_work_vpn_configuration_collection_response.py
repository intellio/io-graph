from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidForWorkVpnConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidForWorkVpnConfiguration]] = Field(alias="value", default=None,)

from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
