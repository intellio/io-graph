from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsWiredNetworkConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsWiredNetworkConfiguration]] = Field(alias="value", default=None,)

from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
