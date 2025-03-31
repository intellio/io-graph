from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsWifiEnterpriseEAPConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsWifiEnterpriseEAPConfiguration]] = Field(alias="value", default=None,)

from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
