from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10XWifiConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10XWifiConfiguration]] = Field(alias="value", default=None,)

from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
